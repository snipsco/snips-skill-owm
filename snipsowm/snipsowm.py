# -*-: coding utf-8 -*-
""" OpenWeatherMap skill for Snips. """

import requests
import json
import pprint

from sentence_generation.sentence_generator import generate_condition_sentence, SentenceTone
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

    def speak_condition(self, condition, locality, date, granularity=0):
        """ Speak a random response for a given weather condition
            at a specified locality and datetime.

        :param condition: A SnipsWeatherCondition value string
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

        if locality is None:
            locality = self.default_location

        # We retrieve the condition and the temperature from our weather provider

        actual_condition, temperature = \
            self.get_current_weather(locality) if date is None else self.get_forecast_weather(locality, date)

        # We now build the sentence

        if condition is None:
            tone = SentenceTone.NEUTRAL
        else:

            assumed_condition = weather_condition.SnipsWeatherCondition(condition).resolve()
            expected_condition = weather_condition.OWMWeatherCondition(actual_condition).resolve()

            tone = SentenceTone.NEGATIVE if assumed_condition.value != expected_condition.value else SentenceTone.NEGATIVE

        generated_sentence = generate_condition_sentence(tone, expected_condition.describe(), locality, date)
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
        print url
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
        :param location:
        :type location:
        :param datetime:
        :type datetime:
        :return:
        :rtype:
        """
        url = "{}?APPID={}&q={}&units=metric".format(self.API_FORECAST_ENDPOINT,
                                                     self.api_key,
                                                     location)
        r = requests.get(url)
        response = json.loads(r.text)

        try:
            pass
        except:
            pass

        return ()

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
        result = {}
        for time_interval in response["list"]:
            current_time = datetime.datetime.strptime(time_interval['dt_txt'], "%Y-%m-%d %H:%M:%S")
            current_delta = date_time - current_time
            if delta > current_delta:
                delta = current_delta
                result = time_interval

        return result

if __name__ == "__main__":
    class STDOut:
        def speak(self, string):
            print string

    std_out = STDOut()


    skill = SnipsOWM("", "Paris", std_out)
    print datetime.datetime(2017, 5, 15)
    with open('/Users/robin/projects/snips/snips_skills/skills/sample_response.json') as data_file:    
        data = json.load(data_file)
    print skill._getTopicalInfos(data, datetime.datetime(2017, 5, 15))
    skill.get_forecast_weather("Madrid", datetime.datetime(2017, 5, 15)) 
    skill.speak_condition('HUMID', 'Paris', None)
