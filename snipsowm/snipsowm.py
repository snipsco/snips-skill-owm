# -*-: coding utf-8 -*-
""" OpenWeatherMap skill for Snips. """

import requests
import json


class SnipsOWM:
    """ OpenWeatherMap skill for Snips. """

    API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"

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

    def execute(self, location=None, datetime=None):
        """Obtain the weather forecast.

        :param location: The location of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :param datetime: Time of the forecast, in ISO 8601 format, e.g.
                         "2017-07-21T10:35:29+00:00"
        """
        (description, temperature) = self.get_weather(location)
        response = self.generate_sentence(location, description, temperature)
        if self.tts_service and response:
            self.tts_service.speak(response)

    def get_weather(self, location):
        """Perform the API request.

        :param location: The location of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        """
        url = "{}?APPID={}&q={}&units=metric".format(self.API_ENDPOINT,
                                                     self.api_key,
                                                     location)
        r = requests.get(url)
        response = json.loads(r.text)
        try:
            description = response["weather"][0]["description"].encode('utf-8')
        except (KeyError, IndexError, UnicodeEncodeError):
            description = None
        try:
            temperature = int(float(response["main"]["temp"]))
        except KeyError:
            temperature = None
        return (description, temperature)

    def generate_sentence(self, location, description, temperature):
        """Generate a sentence for a given weather forecast, e.g. "Weather
           conditions for Chicago: sunny, 23 degrees celcius."

        :param location: The location of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        """
        if location:
            presentation = "Weather conditions for {}".format(location)
        else:
            presentation = "Weather conditions".format(location)

        if description and temperature:
            forecast = "{}, temperature {} degrees celcius".format(
                description, temperature)
        elif description:
            forecast = description
        elif temperature:
            forecast = "temperature {} degrees celcius".format(temperature)
        else:
            forecast = "currently unavailable"

        return "{}: {}".format(presentation, forecast)
