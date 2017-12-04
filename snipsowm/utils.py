# -*- coding: utf-8 -*-

def _convert_to_unix_case(text):
    result = ""
    for i in text:
        if i is ' ' or i is '-':
            result += '_'
        else:
            result += i.capitalize()
    return result
