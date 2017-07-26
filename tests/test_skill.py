from unittest import TestCase

from snipsowm.snipsowm import SnipsOWM


class TestSkill(TestCase):

    def setUp(self):
        self.skill = SnipsOWM("e3deb9f92803fce990166d1af2f3d0fc", "Paris,fr")

    def test_get_weather(self):
        response = self.skill.get_weather("Paris,fr")
        self.assertEqual(len(response), 2)
