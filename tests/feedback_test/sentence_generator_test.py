from unittest import TestCase

import datetime
from snipsowm.feedback import sentence_generator


class TestSentenceGenerator(TestCase):
    def setUp(self):
        pass

    def test_conditionQuerySentenceGenerator(self):
        pass


class TestAnswerSentenceGenerator(TestCase):
    def setUp(self):
        self.generator = sentence_generator.AnswerSentenceGenerator(locale="random")

    def test_sentence_generation_locality_empty(self):
        self.assertEquals(len(self.generator.generate_sentence_locality()), 0)


class TestEnglishAnswerSentenceGenerator(TestCase):
    def setUp(self):
        self.generator = sentence_generator.AnswerSentenceGenerator()

    def test_sentence_generation_locality_empty(self):
        self.assertEquals(len(self.generator.generate_sentence_locality()), 0)

class TestFrenchAnswerSentenceGenerator(TestCase):
    def setUp(self):
        self.generator = sentence_generator.AnswerSentenceGenerator(locale="fr_FR")

    def test_sentence_generation_locality_empty(self):
        self.assertEquals(len(self.generator.generate_sentence_locality()), 0)