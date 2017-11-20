#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from enum import Enum
import locale
import random


class Language(Enum):
    ENGLISH = 0
    FRENCH = 1


class SentenceTone(Enum):
    NEUTRAL = 0
    POSITIVE = 1
    NEGATIVE = 2


def date_to_string(date, granularity=0):
    """ Convert a date to a string, with an appropriate level of
        granularity.

    :param date: A datetime object.
    :param granularity: Granularity for the desired textual representation.
                        0: precise (date and time are returned)
                        1: day (only the week day is returned)
                        2: month (only year and month are returned)
                        3: year (only year is returned)
    :return: A textual representation of the date.
    """
    if not date:
        return None

    if granularity == 0:
        return date.strftime("%A")
    elif granularity == 1:
        return date.strftime("%A, %d")
    elif granularity == 2:
        return date.strftime("%A, %d %B")

    return date.strftime("%A, %d %B, %H:%M%p")


def generate_condition_sentence(tone, condition_description, locality, date):
    """
    The sentence is generated from those parts :
        - introduction (We answer positively or negatively to the user)
        - condition (we describe the condition to the user)
        - date (when is the condition happening)
        - locality (where the condition is happening)

    :param tone:
    :type tone: SentenceTone
    :param condition_description:
    :type condition_description: basestring
    :param locality:
    :type locality:basestring
    :param date:
    :type date:datetime
    :return:
    :rtype:

    """

    # Introduction
    sentence_beginnings = {
        SentenceTone.POSITIVE: "Yes, ",
        SentenceTone.NEGATIVE: "No, ",
        SentenceTone.NEUTRAL: ""

    }

    sentence_beginning = sentence_beginnings[tone]
    sentence_locality = "" if locality is None else " in {}".format(locality)  # Locality
    sentence_date = "" if date is None else " on {}".format(date_to_string(date))  # date

    permutable_parameters = list((sentence_locality, sentence_date))
    random.shuffle(permutable_parameters)
    parameters = (sentence_beginning, condition_description) + tuple(permutable_parameters)

    return "{}{}{}{}".format(*parameters)


def generate_temperature_sentence(temperature, locality, date):
    """
    The sentence is generated from those parts :
        - the temperature for the date and time
        - date (the time when their will be such a temperature )
        - locality (the place their is such a temperature)

    :param temperature
    :param locality:
    :type locality:basestring
    :param date:
    :type date:datetime
    :return:
    :rtype:

    """
    if (temperature is None):
        return "I couldn't fetch the right data for the specified place and date"
    sentence_beginning = "The temperature"

    temperature = "will be " + str(temperature) + " degrees"

    sentence_locality = "" if locality is None else "in {}".format(locality)  # Locality
    sentence_date = "" if date is None else "on {}".format(date_to_string(date))  # date

    time_place_parameters = list((sentence_locality, sentence_date))
    random.shuffle(time_place_parameters)

    time_place_str = time_place_parameters[0] + " " + time_place_parameters[1]

    temp_time_place_params = [time_place_str, temperature]
    random.shuffle(temp_time_place_params)

    return "{} {} {}".format(sentence_beginning, *temp_time_place_params)


def _flatten(array):
    result = []
    for val in array:
        if type(val) is str:
            result += val
        else:
            for sub_val in val:
                result += val
    return result


def french_is_masculine_word(word):
    return word[len(word) - 1] not in ['é','e']


def starts_with_vowel(word):
    return word[0] in ['a', 'e', 'i', 'o', 'u', 'y']


class SentenceGenerator(object):
    def __init__(self, language=Language.ENGLISH):
        """
        :param language:
        :type language: Language
        """
        self.language = language

    def generate_sentence_introduction(self, tone):
        """

        :param tone:
        :type tone: SentenceTone
        :return: an introduction string
        :rtype:basestring
        """

        sentence_beginnings = {
            Language.ENGLISH: {
                SentenceTone.POSITIVE: "Yes, ",
                SentenceTone.NEGATIVE: "No, ",
                SentenceTone.NEUTRAL: ""
            },
            Language.FRENCH: {
                SentenceTone.POSITIVE: "Oui, ",
                SentenceTone.NEGATIVE: "Non, ",
                SentenceTone.NEUTRAL: ""
            }
        }

        sentence_beginning = sentence_beginnings[self.language][tone]
        return sentence_beginning

    def generate_sentence_locality(self, POI=None, Locality=None, Region=None, Country=None):
        """
        :param Locality:
        :type Locality:basestring
        :param POI:
        :type POI:basestring
        :param Region:
        :type Region:basestring
        :param Country:
        :type Country:basestring
        :return:
        :rtype: basestring
        """
        if self.language == Language.ENGLISH:
            return "" if Locality is None else " in {}".format(Locality)
        if self.language == Language.FRENCH:
            """
            Country granularity:
            - We use "au" for masculine nouns that begins with a consonant
            - We use "en" with feminine words and masculine words that start with a vowel
            - Careful with the country Malte. Which is an exception

            Region granularity:
            We use the "en" for regions

            Locality granularity:
            This is used for cities, We use the "à" preposition.

            POIs granularity:
            We use the "à" preposition

            """

            if POI:
                return "à {}".format(POI)

            if Locality:
                return "à {}".format(Locality)

            if Region:
                if french_is_masculine_word(Region) and (not starts_with_vowel(Region)):
                    return "au {}".format(Region)
                else:
                    return "en {}".format(Region)
            if Country:
                if french_is_masculine_word(Country) and (not starts_with_vowel(Country)):
                    return "au {}".format(Country)
                else:
                    return "en {}".format(Country)
        else:
            return ""

    def generate_sentence_date(self,date, granularity=0, language=Language.ENGLISH):
        """ Convert a date to a string, with an appropriate level of
            granularity.

        :param date: A datetime object.
        :param granularity: Granularity for the desired textual representation.
                            0: precise (date and time are returned)
                            1: day (only the week day is returned)
                            2: month (only year and month are returned)
                            3: year (only year is returned)
        :return: A textual representation of the date.
        """
        if (language == Language.FRENCH):
            """
            Careful, this operation is not thread safe ...
            """
            try:
                locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
            except locale.Error:
                return ""

        if not date:
            return ""

        if granularity == 0:
            return date.strftime("%A")
        elif granularity == 1:
            return date.strftime("%A, %d")
        elif granularity == 2:
            return date.strftime("%A, %d %B")

        return date.strftime("%A, %d %B, %H:%M%p")

    def generate_condition_description(self):
        return ""

    def generate_condition_sentence(self):
        """
            The sentence is generated from those parts :
                - introduction (We answer positively or negatively to the user)
                - condition (we describe the condition to the user)
                - date (when is the condition happening)
                - locality (where the condition is happening)

            :param tone:
            :type tone: SentenceTone
            :param condition_description:
            :type condition_description: basestring
            :param locality:
            :type locality:basestring
            :param date:
            :type date:datetime
            :return:
            :rtype:

            """
        sentence = ""
        return sentence


if __name__ == "__main__":
    generator = SentenceGenerator(Language.FRENCH)
    print generator.generate_condition_locality()