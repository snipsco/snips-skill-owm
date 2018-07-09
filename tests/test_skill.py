# -*- coding: utf-8 -*-

import datetime
from unittest import TestCase

from snipsowm.snipsowm import SnipsOWM
from snipsowm.sentence_generator import SentenceGenerator

DUMMY_API_KEY = "dummykey"
DUMMY_LOCATION = "DUMMY LOCATION"


class EnglishTestTemperature(TestCase):

    def setUp(self):
        self.api_key = DUMMY_API_KEY
        self.default_location = DUMMY_LOCATION

    def test_skill_speak_temperature_wrong_api_key(self):
        skill = SnipsOWM(self.api_key, self.default_location, locale="en_US")
        sentence = skill.speak_temperature("Paris", datetime.datetime.now() + datetime.timedelta(hours=+2))
        self.assertEquals(sentence, SentenceGenerator().generate_api_key_error_sentence(), True)


class EnglishTestCondition(TestCase):

    def setUp(self):
        self.api_key = DUMMY_API_KEY
        self.default_location = DUMMY_LOCATION

    def test_skill_speak_condition_wrong_api_key(self):
        skill = SnipsOWM(self.api_key, self.default_location, locale="en_US")
        sentence = skill.speak_temperature("Paris", datetime.datetime.now() + datetime.timedelta(hours=+2))
        self.assertEquals(sentence, SentenceGenerator().generate_api_key_error_sentence(), True)


