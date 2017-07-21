from unittest import TestCase

from snipsowm.snipsowm import SnipsOWM

class TestSkills(TestCase):

    def setUp(self):
        self.skill = SnipsOWM("e3deb9f92803fce990166d1af2f3d0fc", "Paris,fr")

    def test_skill(self):
    	response = self.skill.execute()
        self.assertNotEqual(len(response), 0)
