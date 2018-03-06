# -*- coding: utf-8 -*-

import collections
import datetime
from unittest import TestCase

from utils import MockSnips as Snips, DUMMY_API_KEY, DUMMY_LOCATION
from snipsowm.snipsowm import SnipsOWM
from snipsowm.provider.weather_provider import WeatherProviderError
from snipsowm.provider.owm_provider import OpenWeatherMapAPIKeyError

class EnglishTestTemperature(TestCase):

    def setUp(self):
        self.mocked_snips = Snips()
        self.api_key = DUMMY_API_KEY
        self.default_location = "Paris, fr"

    def test_skill_speak_temperature_wrong_api_key(self):
        skill = SnipsOWM(self.api_key, self.default_location, locale="en_US")
        skill.speak_temperature(self.mocked_snips, "Paris", datetime.datetime.now() + datetime.timedelta(hours=+2))
        self.assertEquals(self.mocked_snips.dialogue._speak_called, True)


class EnglishTestCondition(TestCase):

    def setUp(self):
        self.mocked_snips = Snips()
        self.default_location = "Paris, fr"
        self.api_key = DUMMY_API_KEY

    def test_skill_speak_condition_wrong_api_key(self):
        skill = SnipsOWM(self.api_key, self.default_location, locale="en_US")
        skill.speak_temperature(self.mocked_snips, "Paris", datetime.datetime.now() + datetime.timedelta(hours=+2))
        self.assertEquals(self.mocked_snips.dialogue._speak_called, True)


