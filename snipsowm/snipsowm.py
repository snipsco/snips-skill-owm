# -*-: coding utf-8 -*-
""" OpenWeatherMap skill for Snips. """

import requests
import json
import pprint

from sentence_generation.sentence_generator import generate_condition_sentence, generate_temperature_sentence, SentenceTone
from ontology import weather_condition, snips, owm
import datetime


class SnipsOWM:
    """ OpenWeatherMap skill for Snips. """

    API_WEATHER_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
    API_FORECAST_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key, default_location, tts_service=None):
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

        generated_sentence = generate_temperature_sentence(temperature, locality, date)

        if self.tts_service is not None:
            self.tts_service.speak(generated_sentence)


    def speak_condition(self, assumed_condition, locality, date, granularity=0):
        """ Speak a random response for a given weather condition
            at a specified locality and datetime.

        :param assumed_condition: A SnipsWeatherCondition value string
                          corresponding to a weather condition extracted from the slots.
                          e.g 'HUMID', 'SUNNY', etc ... 
        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :type locality: string

        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00"
        :type date: datetime

        :return: A random response for a given weather condition
                 at a specified locality and datetime.
        """

        # We initialize variables

        actual_condition_group = weather_condition.WeatherCondition( weather_condition.WeatherConditions.UNKNOWN )
        assumed_condition_group = weather_condition.WeatherCondition( weather_condition.WeatherConditions.UNKNOWN )
        tone = SentenceTone.NEUTRAL
        if locality is None:
            locality = self.default_location

        # We retrieve the condition and the temperature from our weather provider

        actual_condition, temperature = \
            self.get_current_weather(locality) if date is None else self.get_forecast_weather(locality, date)

        # We find the categorie (group) of the received weather description

        assumed_condition_group = weather_condition.SnipsWeatherCondition(assumed_condition).resolve()
        actual_condition_group = weather_condition.OWMWeatherCondition(actual_condition).resolve()

        # We check if their is a positive/negative tone to add to the answer

        if assumed_condition_group.value != weather_condition.WeatherConditions.UNKNOWN:
            tone = SentenceTone.NEGATIVE if assumed_condition_group.value != actual_condition_group.value else SentenceTone.POSITIVE

        # We compose the sentence

        generated_sentence = generate_condition_sentence(tone, actual_condition_group.describe(), locality, date)
        # print "[generated sentence] " + generated_sentence

        # And finally send it to the TTS if provided

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

    skill = SnipsOWM("e3deb9f92803fce990166d1af2f3d0fc", "Paris", std_out)

    print "\n speak condition: \n"

    skill.speak_condition('HUMID', 'Paris', datetime.datetime(2017, 5, 15))
    skill.speak_condition('BLIZZARD', 'Lyon', None)
    skill.speak_condition('NOTKNOWN', 'Paris', None)
    skill.speak_condition('CLOUD', 'Paris', datetime.datetime(2017, 5, 15))
    skill.speak_condition('CLOUD', 'Lyon', datetime.datetime(2017, 11, 1))
    skill.speak_condition('CLOUD', 'Lyon', datetime.datetime(2017, 11, 5))
    skill.speak_condition('CLOUDY', 'Paris', None)
    skill.speak_condition('SUNNY', None, None)
    skill.speak_condition(None, None, None)

    print "\n\n\n speak temperature: \n"

    skill.speak_temperature('Paris', datetime.datetime(2017, 11, 1))
    skill.speak_temperature('Paris', datetime.datetime(2017, 5, 15))
    skill.speak_temperature('Lyon', None)
    skill.speak_temperature('Madrid', None)
    skill.speak_temperature(None, None)

    print "\n\n\n speak item: \n"

    skill.speak_condition('Raincoat', 'Paris', datetime.datetime(2017, 5, 15))
    skill.speak_condition('Sunglasses', 'Lyon', datetime.datetime(2017, 11, 1))
    skill.speak_condition('Chunky Sweater', 'Lyon', datetime.datetime(2017, 11, 5))
