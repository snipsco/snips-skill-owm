# -*- coding: utf-8 -*-

def _convert_to_unix_case(text):
    return text.replace(' ', '_').replace('-', '_').upper()
