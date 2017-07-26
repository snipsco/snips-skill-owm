from unittest import TestCase

from snipsowm.snipsowm import SnipsOWM


class TestSkill(TestCase):

    def setUp(self):
        self.skill = SnipsOWM("***REMOVED***", "Paris,fr")

    def test_get_weather(self):
        response = self.skill.get_weather("Paris,fr")
        self.assertEqual(len(response), 2)
