# -*- coding: utf-8 -*-
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