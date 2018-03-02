# -*- coding: utf-8 -*-
""" OpenWeatherMap skill for Snips. """

import datetime
import json
import requests
from sentence_generator import SentenceTone, SentenceGenerator
from provider.providers import WeatherProviders
from provider.weather_provider import WeatherProviderError, WeatherProviderConnectivityError
import weather_condition


class SnipsOWM:
    """ OpenWeatherMap skill for Snips. """




    def __init__(self, api_key, default_location, locale="en_US"):
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
        self.locale = locale

        self.provider = WeatherProviders.OWM(api_key)

    def speak_temperature(self, snips, locality, date, granularity=0):
        """ Tell the temperature at a given locality and datetime.

        :param locality: The locality of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        :type locality: string

        :param date: Time of the forecast, in ISO 8601 format, e.g.
                     "2017-07-21T10:35:29+00:00"
        :type date: datetime

        :return: The temperature at a given locality and datetime.
        """
        sentence_generator = SentenceGenerator(locale=self.locale)

        try:
            if locality is None:
                locality = self.default_location
            actual_condition, temperature = \
                self.provider.get_current_weather(locality) if date is None else self.provider.get_forecast_weather(locality, date)

            generated_sentence = sentence_generator.generate_temperature_sentence(temperature=temperature,
                                                                              date=date, granularity=0,
                                                                              Locality=locality)


        except WeatherProviderError:
            generated_sentence = sentence_generator.generate_error_sentence()

        snips.dialogue.speak(generated_sentence, snips.session_id)

    def speak_condition(self, snips, assumed_condition, date, POI=None, Locality=None, Region=None, Country=None,
                        granularity=0):
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
        assumed_condition_group = weather_condition.WeatherConditionDescriptor(weather_condition.WeatherConditions.UNKNOWN)
        tone = SentenceTone.NEUTRAL

        # We retrieve the condition and the temperature from our weather provider
        actual_condition_group = weather_condition.WeatherConditionDescriptor(weather_condition.WeatherConditions.UNKNOWN)

        sentence_generator = SentenceGenerator(locale=self.locale)
        try:
            actual_condition, temperature = \
                self.provider.get_current_weather(locality) if date == now_date else self.provider.get_forecast_weather(locality, date)

            # We retrieve the weather from our weather provider
            actual_condition_group = weather_condition.OWMToWeatherConditionMapper(actual_condition).resolve()

            if assumed_condition:
                # We find the category (group) of the received weather description
                assumed_condition_group = weather_condition.SnipsToWeatherConditionMapper().fuzzy_matching(self.locale, assumed_condition).resolve()

                # We check if their is a positive/negative tone to add to the answer
                if assumed_condition_group.value != weather_condition.WeatherConditions.UNKNOWN:
                    tone = SentenceTone.NEGATIVE if assumed_condition_group.value != actual_condition_group.value else SentenceTone.POSITIVE
            else:
                tone = SentenceTone.NEUTRAL

            # We compose the sentence
            generated_sentence = sentence_generator.generate_condition_sentence(tone=tone,
                                                                                date=date, granularity=granularity,
                                                                                condition_description=actual_condition_group.describe(
                                                                                    self.locale),
                                                                                POI=POI, Locality=Locality,
                                                                                Region=Region,
                                                                                Country=Country)

            # And finally send it to the TTS if provided
        except WeatherProviderError as e:
            generated_sentence = sentence_generator.generate_error_sentence()

        snips.dialogue.speak(generated_sentence, snips.session_id)
