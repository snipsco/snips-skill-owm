from unittest import TestCase

from snipsowm.snipsowm import SnipsOWM

class TestSkills(TestCase):

    def setUp(self):
        self.skill = SnipsOWM("***REMOVED***", "Paris,fr")

    def test_skill(self):
    	response = self.skill.execute()
        self.assertNotEqual(len(response), 0)
