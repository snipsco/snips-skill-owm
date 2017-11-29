# -*- coding: utf-8 -*-
""" OpenWeatherMap skill for Snips. """

import datetime
import json

import requests
import weather_condition
from sentence_generator import SentenceTone, SentenceGenerator


class SnipsOWM:
    """ OpenWeatherMap skill for Snips. """

    API_WEATHER_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
    API_FORECAST_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"

    OWM_MAX_FORECAST_DAYS = 15

    def __init__(self, api_key, default_location, tts_service=None, locale="en_US"):
        """
        :param api_key: OpenWeatherMap API key.
        :param default_location: Default location for which to fetch the
                                 weather when none is provided.
        :param tts: Optionally, a Text-to-Speech for speaking the weather
                    results. Such a service should expose a `speak(phrase)`
                    method.
        """
        self.api_key = api_key
        self.default_location = default_location
        self.tts_service = tts_service
        self.locale = locale

    def speak_temperature(self, locality, date, granularity=0):
        """ Tell the temperature at a given locality and datetime.

        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :type locality: string

        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00"
        :type date: datetime

        :return: The temperature at a given locality and datetime.
        """
        if locality is None:
            locality = self.default_location
        actual_condition, temperature = \
            self.get_current_weather(locality) if date is None else self.get_forecast_weather(locality, date)

        sentence_generator = SentenceGenerator(locale=self.locale)
        generated_sentence = sentence_generator.generate_temperature_sentence(temperature=temperature,
                                                                              date=date, granularity=0,
                                                                              Locality=locality)

        if self.tts_service is not None:
            self.tts_service.speak(generated_sentence)

    def speak_condition(self, assumed_condition, date, POI=None, Locality=None, Region=None, Country=None, granularity=0):
        """ Speak a response for a given weather condition
            at a specified locality and datetime.
            If the locality is not specified, use the default location.

        :param assumed_condition: A SnipsWeatherCondition value string
                          corresponding to a weather condition extracted from the slots.
                          e.g 'HUMID', 'SUNNY', etc ...
                          Can be none, if there is no assumption.
        :type assumed_condition: basestring

        :param date: datetime of the forecast
        :type date: datetime.datetime

        :param POI: Slot value from Snips
        :type POI: basestring

        :param Locality: Slot value from Snips
        :type Locality: basestring

        :param Region: Slot value from Snips
        :type Region: basestring

        :param Country: Slot value from Snips
        :type Country: basestring

        :param granularity: Precision with which the date should be described.
        :type granularity: int

        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """

        # If the forecast date is higher than 16 days (which is OWM limit), don't tell the weather.
        now_date = datetime.datetime.now()

        if date is None:
            date = now_date

        if date < now_date or (date - now_date).days > self.OWM_MAX_FORECAST_DAYS:
            return

        # Checking the parameters values
        if (POI or Locality or Region or Country):
            localities = filter(lambda x: x is not None, [POI, Locality, Region, Country])
            locality = localities[0]
        else:
            locality = self.default_location
            Locality = self.default_location

        # Initializing variables
        actual_condition_group = weather_condition.WeatherCondition(weather_condition.WeatherConditions.UNKNOWN)
        assumed_condition_group = weather_condition.WeatherCondition(weather_condition.WeatherConditions.UNKNOWN)
        tone = SentenceTone.NEUTRAL

        # We retrieve the condition and the temperature from our weather provider
        actual_condition, temperature = \
            self.get_current_weather(locality) if date == now_date else self.get_forecast_weather(locality, date)


        # We retrieve the weather from our weather provider
        actual_condition_group = weather_condition.OWMWeatherCondition(actual_condition).resolve()

        if assumed_condition:
            # We find the category (group) of the received weather description
            assumed_condition_group = weather_condition.SnipsWeatherCondition(assumed_condition).resolve()

            # We check if their is a positive/negative tone to add to the answer
            if assumed_condition_group.value != weather_condition.WeatherConditions.UNKNOWN:
                tone = SentenceTone.NEGATIVE if assumed_condition_group.value != actual_condition_group.value else SentenceTone.POSITIVE
        else:
            tone = SentenceTone.NEUTRAL

        # We compose the sentence
        sentence_generator = SentenceGenerator(locale=self.locale)
        generated_sentence = sentence_generator.generate_condition_sentence(tone=tone,
                                                                            date=date, granularity=granularity,
                                                                            condition_description=actual_condition_group.describe(self.locale),
                                                                            POI=POI, Locality=Locality, Region=Region, Country=Country)

        # And finally send it to the TTS if provided

        print generated_sentence
        if self.tts_service is not None:
            self.tts_service.speak(generated_sentence)

    def get_current_weather(self, location):
        """Perform the API request.

        :param location: The location of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        """
        url = "{}?APPID={}&q={}&units=metric".format(self.API_WEATHER_ENDPOINT,
                                                     self.api_key,
                                                     location)
        r = requests.get(url)
        response = json.loads(r.text)
        try:
            description = response["weather"][0]["id"]
        except (KeyError, IndexError, UnicodeEncodeError):
            description = None
        try:
            temperature = int(float(response["main"]["temp"]))
        except KeyError:
            temperature = None
        return (description, temperature)

    def get_forecast_weather(self, location, datetime):
        """
        Perform the API request.
        :param location: The location of the asked forecast 
        :type location: string 
        :param datetime: The date and time of the requested forecast
        :type datetime: datetime
        :return: description of the asked weather and the temperature
        :rtype: (str, int)
        """
        url = "{}?APPID={}&q={}&units=metric".format(self.API_FORECAST_ENDPOINT,
                                                     self.api_key,
                                                     location)
        r = requests.get(url)
        response = json.loads(r.text)
        response = self._getTopicalInfos(response, datetime)

        try:
            description = response["weather"][0]["id"]
        except (KeyError, IndexError, UnicodeEncodeError):
            description = None
        try:
            temperature = int(float(response["main"]["temp"]))
        except KeyError:
            temperature = None
        return (description, temperature)

    def get_weather(self, location, datetime=None):
        if datetime:
            return self.get_forecast_weather(location, datetime)
        else:
            return self.get_current_weather(location)

    @staticmethod
    def generate_forecast_temperature_sentence():
        pass

    @staticmethod
    def generate_forecast():
        pass

    def _getTopicalInfos(self, response, date_time):
        delta = date_time - datetime.datetime.strptime(response["list"][0]['dt_txt'], "%Y-%m-%d %H:%M:%S")
        delta = abs(delta)
        result = {}

        for time_interval in response["list"]:
            current_time = datetime.datetime.strptime(time_interval['dt_txt'], "%Y-%m-%d %H:%M:%S")
            current_delta = date_time - current_time
            current_delta = abs(current_delta)
            if delta > current_delta:
                delta = current_delta
                result = time_interval

        return result


if __name__ == "__main__":
    class STDOut:
        def speak(self, string):
            print string


    std_out = STDOut()

    skill = SnipsOWM("e75d39d94de1e2fa6aad857646f9b5a1", "Paris", std_out, locale="fr_FR")

    skill.speak_condition(None, datetime.datetime(2017, 11, 30), Locality='Berlin')
