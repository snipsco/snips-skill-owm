# -*- coding: utf-8 -*-
from enum import Enum


# These are the reference weather conditions.
class WeatherConditions(Enum):
    UNKNOWN = 0
    DRIZZLE = 1
    RAIN = 2
    SNOW = 3
    FOG = 4
    SUN = 5
    CLOUDS = 6
    STORM = 7
    HUMID = 8
    WIND = 9
    THUNDERSTORM = 10
