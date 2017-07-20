#!/usr/bin/env python3
# encoding: utf-8

import requests
import json


class Weather:

    API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"

    ACCEPTED_INTENTS = [
        "SearchWeatherForecast",
        "SearchWeatherForecastCondition"
    ]

    def __init__(self, api_key, default_location, tts_service=None):
        self.api_key = api_key
        self.default_location = default_location
        self.tts_service = tts_service

    ###########################################################################
    # Intent handler
    ###########################################################################

    def handle_intent(self, intent):
        if not self.get_intent_name(intent) in self.ACCEPTED_INTENTS:
            return
        location = self.get_slot_value(intent, "weatherForecastLocality") \
            or self.get_slot_value(intent, "weatherForecastCountry") \
            or self.get_slot_value(intent, "weatherForecastGeographicalPOI") \
            or self.default_location
        (description, temperature) = self.get_weather(location)
        response = self.generate_sentence(location, description, temperature)
        if self.tts_service and response:
            self.tts_service.speak(response)

    ###########################################################################
    # Parsing functions
    ###########################################################################

    def get_intent_name(self, intent):
        if 'intent' in intent and 'intentName' in intent['intent']:
            return intent['intent']['intentName'].split('__')[-1]
        return None

    def get_slot_value(self, intent, slot_name):
        try:
            slot = next(s for s in intent['slots']
                        if s['slotName'] == slot_name)
            if 'value' in slot and 'value' in slot['value']:
                if 'value' in slot['value']['value']:
                    return slot['value']['value']['value']
                return slot['value']['value']
        except StopIteration:
            pass
        return None

    ###########################################################################
    # API
    ###########################################################################

    def get_weather(self, location):
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

    ###########################################################################
    # Response generation
    ###########################################################################

    def generate_sentence(self, location, description, temperature):
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
