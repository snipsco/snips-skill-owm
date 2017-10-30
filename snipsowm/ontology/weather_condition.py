from enum import Enum
from owm import OWMWeatherConditions
from snips import SnipsWeatherConditions
import random


class WeatherConditions(Enum):
    THUNDERSTORM = 0
    DRIZZLE = 1
    RAIN = 2
    SNOW = 3
    FOG = 4
    SUN = 5
    CLOUDS = 6
    STORM = 7
    HUMID = 8
    WIND = 9
    UNKNOWN = 10


class WeatherCondition(object):
    def __init__(self, key):
        self.value = key

    descriptions = {
        WeatherConditions.THUNDERSTORM : ["Thunderstorms are expected","expect thunderstorms"],
        WeatherConditions.DRIZZLE : ["drizzle are expected","expect drizzle"],
        WeatherConditions.RAIN : ["rain is expected","it's going to be rainy","expect rain"],
        WeatherConditions.SNOW : ["snow is expected","it's going to snow","expect snow"],
        WeatherConditions.FOG : ["fog is expected","it's going to be foggy","expect fog"],
        WeatherConditions.SUN : ["sun is expected","it's going to be sunny"],
        WeatherConditions.CLOUDS : ["it's going to be cloudy","expect clouds"],
        WeatherConditions.STORM : ["storms are expected","it's going to be stormy","expect storms"],
        WeatherConditions.HUMID : ["humidity is expected","it's going to be humid"],
        WeatherConditions.WIND : ["wind is expected","it's going to be windy","expect wind"],
        WeatherConditions.UNKNOWN : [""]
    }

    def describe(self):
        return random.choice(self.descriptions[self.value])


class SnipsWeatherCondition(object):
    mappings = {
        SnipsWeatherConditions.HUMID: WeatherConditions.HUMID,
        SnipsWeatherConditions.BLIZZARD: WeatherConditions.UNKNOWN,
        SnipsWeatherConditions.SNOWFALL: WeatherConditions.SNOW,
        SnipsWeatherConditions.WINDY: WeatherConditions.WIND,
        SnipsWeatherConditions.CLOUD: WeatherConditions.CLOUDS,
        SnipsWeatherConditions.RAINY: WeatherConditions.RAIN,
        SnipsWeatherConditions.STORMY: WeatherConditions.STORM,
        SnipsWeatherConditions.SUN: WeatherConditions.SUN,
        SnipsWeatherConditions.SNOW: WeatherConditions.SNOW,
        SnipsWeatherConditions.FOG: WeatherConditions.FOG,
        SnipsWeatherConditions.DEPRESSION: WeatherConditions.RAIN,
        SnipsWeatherConditions.STORM: WeatherConditions.STORM,
        SnipsWeatherConditions.RAINFALL: WeatherConditions.RAIN,
        SnipsWeatherConditions.SNOWY: WeatherConditions.SNOW,
        SnipsWeatherConditions.SUNNY: WeatherConditions.SUN,
        SnipsWeatherConditions.RAIN: WeatherConditions.RAIN,
        SnipsWeatherConditions.HAIL: WeatherConditions.UNKNOWN,
        SnipsWeatherConditions.FOGGY: WeatherConditions.FOG,
        SnipsWeatherConditions.OVERCAST: WeatherConditions.CLOUDS,
        SnipsWeatherConditions.CLOUDY: WeatherConditions.CLOUDS,
        SnipsWeatherConditions.HUMIDITY: WeatherConditions.HUMID,
        SnipsWeatherConditions.SNOWSTORM: WeatherConditions.SNOW,
        SnipsWeatherConditions.WIND: WeatherConditions.WIND
    }

    def __init__(self, key):
        self.value = SnipsWeatherConditions[key]

    def resolve(self):
        return WeatherCondition(self.mappings[self.value])


class OWMWeatherCondition(object):
    mappings = {
        OWMWeatherConditions.THUNDERSTORM_WITH_LIGHT_RAIN: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.THUNDERSTORM_WITH_RAIN: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.THUNDERSTORM_WITH_HEAVY_RAIN: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.LIGHT_THUNDERSTORM: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.THUNDERSTORM: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.HEAVY_THUNDERSTORM: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.RAGGED_THUNDERSTORM: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.THUNDERSTORM_WITH_LIGHT_DRIZZLE: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.THUNDERSTORM_WITH_DRIZZLE: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.THUNDERSTORM_WITH_HEAVY_DRIZZLE: WeatherConditions.THUNDERSTORM,
        OWMWeatherConditions.LIGHT_INTENSITY_DRIZZLE: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.DRIZZLE: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.HEAVY_INTENSITY_DRIZZLE: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.LIGHT_INTENSITY_DRIZZLE_RAIN: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.DRIZZLE_RAIN: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.HEAVY_INTENSITY_DRIZZLE_RAIN: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.SHOWER_RAIN_AND_DRIZZLE: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.HEAVY_SHOWER_RAIN_AND_DRIZZLE: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.SHOWER_DRIZZLE: WeatherConditions.DRIZZLE,
        OWMWeatherConditions.LIGHT_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.MODERATE_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.HEAVY_INTENSITY_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.VERY_HEAVY_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.EXTREME_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.FREEZING_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.LIGHT_INTENSITY_SHOWER_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.SHOWER_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.HEAVY_INTENSITY_SHOWER_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.RAGGED_SHOWER_RAIN: WeatherConditions.RAIN,
        OWMWeatherConditions.LIGHT_SNOW: WeatherConditions.SNOW,
        OWMWeatherConditions.SNOW: WeatherConditions.SNOW,
        OWMWeatherConditions.HEAVY_SNOW: WeatherConditions.SNOW,
        OWMWeatherConditions.SLEET: WeatherConditions.SNOW,
        OWMWeatherConditions.SHOWER_SLEET: WeatherConditions.RAIN,
        OWMWeatherConditions.LIGHT_RAIN_AND_SNOW: WeatherConditions.RAIN,
        OWMWeatherConditions.RAIN_AND_SNOW: WeatherConditions.RAIN,
        OWMWeatherConditions.LIGHT_SHOWER_SNOW: WeatherConditions.SNOW,
        OWMWeatherConditions.SHOWER_SNOW: WeatherConditions.SNOW,
        OWMWeatherConditions.HEAVY_SHOWER_SNOW: WeatherConditions.SNOW,
        OWMWeatherConditions.MIST: WeatherConditions.FOG,
        OWMWeatherConditions.SMOKE: WeatherConditions.FOG,
        OWMWeatherConditions.HAZE: WeatherConditions.FOG,
        OWMWeatherConditions.SAND_DUST_WHIRLS: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.FOG: WeatherConditions.FOG,
        OWMWeatherConditions.SAND: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.DUST: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.VOLCANIC_ASH: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.SQUALLS: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.TORNAD: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.FEW_CLOUDS: WeatherConditions.CLOUDS,
        OWMWeatherConditions.SCATTERED_CLOUDS: WeatherConditions.CLOUDS,
        OWMWeatherConditions.BROKEN_CLOUDS: WeatherConditions.CLOUDS,
        OWMWeatherConditions.OVERCAST_CLOUDS: WeatherConditions.CLOUDS
    }

    def __init__(self, id):
        self.value = OWMWeatherConditions(id)

    def resolve(self):
        return WeatherCondition(self.mappings[self.value])



