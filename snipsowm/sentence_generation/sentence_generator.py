import datetime
from enum import Enum
import random


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

    time_place_str = time_place_parameters[0] + " " +time_place_parameters[1]

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


if __name__ == "__main__":
    print generate_temperature_sentence("8", "Paris", datetime.datetime(2017, 11, 1))
    print generate_temperature_sentence("8", "Paris", datetime.datetime(2017, 11, 1))
    print generate_temperature_sentence("8", "Paris", datetime.datetime(2017, 11, 1))
    print generate_temperature_sentence("8", "Paris", datetime.datetime(2017, 11, 1))
    print generate_temperature_sentence("8", "Paris", datetime.datetime(2017, 11, 1))
    print generate_temperature_sentence("8", "Paris", datetime.datetime(2017, 11, 1))

    print generate_condition_sentence(SentenceTone.POSITIVE, "sun is expected", "Paris", None)
    print generate_condition_sentence(SentenceTone.NEGATIVE, "it's going to be raining", "Paris", datetime.datetime(2017, 11, 10))
    print generate_condition_sentence(SentenceTone.NEUTRAL, "fog is expected", "Moscow", datetime.datetime(2017, 11, 10))

