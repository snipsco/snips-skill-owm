#!/usr/bin/env python2
# -*-: coding utf-8 -*-

import ConfigParser
from datetime import datetime
import datetime as dt
from dateutil.parser import parse
from hermes_python.hermes import Hermes
import hermes_python
import io
import os
import sys
from snipsowm.snipsowm import SnipsOWM

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

DIR = os.path.dirname(os.path.realpath(__file__)) + '/alarm/'

lang = "EN"


class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section: dict(self.items(section)) for section in self.sections()}

def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error):
        return dict()

def getCondition(snips):
      # Determine condition
    if snips.slots.forecast_condition_name:
        res = snips.slots.forecast_condition_name[0].slot_value.value.value
        return unicode(res)
    return None

def getLocality(snips):
    if snips.slots.forecast_locality:
        res = snips.slots.forecast_locality[0].slot_value.value.value
        return unicode(res)
    return None

def getRegion(snips):
    if snips.slots.forecast_region:
        res = snips.slots.forecast_region[0].slot_value.value.value
        return unicode(res)
    return None

def getCountry(snips):
    if snips.slots.forecast_country :
        res = snips.slots.forecast_country[0].slot_value.value.value
        return unicode(res)
    return None

def getPOI(snips):
    if snips.slots.forecast_geographical_poi:
        res = snips.slots.forecast_geographical_poi[0].slot_value.value.value
        return unicode(res)
    return None

def getItemName(snips):
    if snips.slots.forecast_item:
        res = snips.slots.forecast_item[0].slot_value.value.value
        return unicode(res)
    return None

def getDateTime(snips):
    # Determine datetime
    if snips.slots.forecast_start_datetime:
        tmp = snips.slots.forecast_start_datetime[0].slot_value.value
        if tmp is None:
            return None
        if isinstance(tmp, hermes_python.ontology.dialogue.InstantTimeValue ):
            val = tmp.value[:-7]
            return datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
        elif isinstance(tmp, hermes_python.ontology.dialogue.TimeIntervalValue ):
            t0 = tmp.from_date[:-7]
            t0 = datetime.strptime(t0, '%Y-%m-%d %H:%M:%S')
            t1 = tmp.to_date[:-7]
            t1 = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
            delta = t1 - t0
            return t0 + delta / 2
    return None

def getAnyLocality(snips):
    locality = None
    try:
        locality = snips.slots.forecast_locality \
          or snips.slots.forecast_country \
          or snips.slots.forecast_region \
          or snips.slots.forecast_geographical_poi

        if locality:
          return unicode(locality[0].slot_value.value.value)
    except Exception:
        pass

def getGranurality(datetime):
    # Determine granularity
    if datetime:  # We have an information about the date.
        now = dt.datetime.now().replace(tzinfo=None)
        delta_days = abs((datetime - now).days)
        if delta_days > 10: # There a week difference between today and the date we want the forecast.
            return 2 # Give the day of the forecast date, plus the number of the day in the month.
        elif delta_days > 5: # There a 10-day difference between today and the date we want the forecast.
            return 1 # Give the full date
        else:
            return 0 # Just give the day of the week
    else:
        return 0

def searchWeatherForecastTemperature(hermes, intent_message):
    datetime = getDateTime(intent_message)
    granularity = getGranurality(datetime)
    locality = getAnyLocality(intent_message)
    res = hermes.skill.speak_temperature(locality, datetime, granularity)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, res.decode("latin-1"))

def searchWeatherForecastCondition(hermes, intent_message):
    datetime = getDateTime(intent_message)
    granularity = getGranurality(datetime)
    condition = getCondition(intent_message)
    locality = getLocality(intent_message)
    region = getRegion(intent_message)
    country = getCountry(intent_message)
    geographical_poi = getPOI(intent_message)
    res = hermes.skill.speak_condition(condition, datetime,
                               granularity=granularity, Locality=locality,
                               Region=region, Country=country,
                               POI=geographical_poi)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, res.decode("latin-1"))

def searchWeatherForecast(hermes, intent_message):
    datetime = getDateTime(intent_message)
    granularity = getGranurality(datetime)
    # No condition in this intent so initialized to None
    condition_name = None
    locality = getLocality(intent_message)
    region = getRegion(intent_message)
    country = getCountry(intent_message)
    geographical_poi = getPOI(intent_message)
    res = hermes.skill.speak_condition(condition_name, datetime,
                               granularity=granularity, Locality=locality,
                               Region=region, Country=country,
                               POI=geographical_poi)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, res.decode("latin-1"))

def searchWeatherForecastItem(hermes, intent_message):
    datetime = getDateTime(intent_message)
    granularity = getGranurality(datetime)
    item_name = getItemName(intent_message)
    locality = getLocality(intent_message)
    region = getRegion(intent_message)
    country = getCountry(intent_message)
    geographical_poi = getPOI(intent_message)
    res = hermes.skill.speak_condition(item_name,
                                  datetime,
                                  granularity=granularity,
                                  Locality=locality,
                                  Region=region,
                                  Country=country,
                                  POI=geographical_poi)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, res.decode("latin-1"))

if __name__ == "__main__":
    config = read_configuration_file("config.ini")

    api_key = config.get("secret", {}).get("api_key")
    if not api_key:
        print("No API key in config.ini, you must setup an OpenWeatherMap API key for this skill to work")
        sys.exit(1)
    
    skill_locale = config["secret"].get("locale")
    if not skill_locale:
        print("No locale information is found!")
        print("Please edit 'config.ini' file, give either en_US, fr_FR or es_ES refering to the language of your assistant")
        sys.exit(1)

    # TODO config["secret"]["default_location"] can be empty is this intended?
    skill = SnipsOWM(api_key, config["secret"]["default_location"], locale=skill_locale.decode('ascii'))

    lang = "EN"
    with Hermes(MQTT_ADDR.encode("ascii")) as h:
        h.skill = skill
        h.subscribe_intent("searchWeatherForecastItem",
                          searchWeatherForecastItem) \
        .subscribe_intent("searchWeatherForecastTemperature",
                          searchWeatherForecastTemperature) \
        .subscribe_intent("searchWeatherForecastCondition",
                          searchWeatherForecastCondition) \
        .subscribe_intent("searchWeatherForecast", searchWeatherForecast) \
        .loop_forever()
