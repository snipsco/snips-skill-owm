#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from enum import Enum
import locale
import random
from utils import _convert_to_unix_case


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
        return ""

    if granularity == 0:
        return date.strftime("%A")
    elif granularity == 1:
        return date.strftime("%A, %d")
    elif granularity == 2:
        return date.strftime("%A, %d %B")

    return date.strftime("%A, %d %B, %H:%M%p")


def french_is_masculine_word(word):
    return word[len(word) - 1] not in ['é', 'e']


def starts_with_vowel(word):
    return word[0] in ['a', 'e', 'i', 'o', 'u', 'y']


class SentenceGenerator(object):
    def __init__(self, locale="en_US"):
        """
        :param language:
        :type language: Language
        """
        self.locale = locale

    def generate_sentence_introduction(self, tone):
        """

        :param tone:
        :type tone: SentenceTone
        :return: an introduction string
        :rtype:basestring
        """

        sentence_beginnings = {
            "en_US": {
                SentenceTone.POSITIVE: "Yes,",
                SentenceTone.NEGATIVE: "No,",
                SentenceTone.NEUTRAL: ""
            },
            "fr_FR": {
                SentenceTone.POSITIVE: "Oui,",
                SentenceTone.NEGATIVE: "Non,",
                SentenceTone.NEUTRAL: ""
            }
        }

        sentence_beginning = sentence_beginnings[self.locale][tone]
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
        if self.locale == "en_US":
            if (POI or Locality or Region or Country):
                locality = filter(lambda x: x is not None, [POI, Locality, Region, Country])[0]
                return "in {}".format(locality)
            else:
                return ""

        if self.locale == "fr_FR":
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

            return ""

        else:
            return ""

    def generate_sentence_date(self, date, granularity=0):
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

        full_locale = "{}.UTF-8".format(self.locale)

        try:  # Careful, this operation is not thread safe ...
            locale.setlocale(locale.LC_TIME, full_locale)
        except locale.Error:
            print "Careful ! There was an error while trying to set the locale. This means your locale is not properly installed. Please refer to the README for more information."
            return ""

        return date_to_string(date, granularity)

    def generate_condition_description(self, condition_description):
        return condition_description if len(condition_description) > 0 else ""

    def generate_condition_sentence(self,
                                    tone=SentenceTone.POSITIVE,
                                    date=None, granularity=0,
                                    condition_description=None,
                                    POI=None, Locality=None, Region=None, Country=None):
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
        introduction = self.generate_sentence_introduction(tone)

        locality = self.generate_sentence_locality(POI, Locality, Region, Country)

        date = self.generate_sentence_date(date, granularity=granularity)

        permutable_parameters = list((locality, date))
        random.shuffle(permutable_parameters)
        parameters = (introduction, condition_description) + tuple(permutable_parameters)

        # Formatting
        parameters = filter(lambda x: not x is None and len(x) > 0, parameters)
        return ("{} " * len(parameters)).format(*parameters)

    def generate_temperature_sentence(self,
                                      temperature="-273.15",
                                      date=None, granularity=0,
                                      POI=None, Locality=None, Region=None, Country=None):
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
        error_sentences = {
            "en_US": "I couldn't fetch the right data for the specified place and date",
            "fr_FR": "Je n'ai pas pu récupérer les prévisions de température pour cet endroit et ces dates"
        }

        if (temperature is None):
            return error_sentences[self.locale]

        sentence_introductions = {
            "en_US": ["The temperature will be {} degrees"],
            "fr_FR": ["La température sera de {} degrés", "Il fera {} degrés"]
        }

        introduction = random.choice(sentence_introductions[self.locale]).format(temperature)
        locality = self.generate_sentence_locality(POI, Locality, Region, Country)
        date = self.generate_sentence_date(date)

        permutable_parameters = list((locality, date))
        random.shuffle(permutable_parameters)
        parameters = (introduction,) + tuple(permutable_parameters)
        return "{} {} {}".format(*parameters)

    def generate_error_sentence(self):
        error_sentences = {
            "en_US": "An error occured when trying to retrieve the weather, please try again",
            "fr_FR": "Désolé, il y a eu une erreur lors de la récupération des données météo. Veuillez réessayer"
        }

        return error_sentences[self.locale]