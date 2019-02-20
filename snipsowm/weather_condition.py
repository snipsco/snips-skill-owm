# -*- coding: utf-8 -*-
from wagnerfischerpp import WagnerFischer
from snips import SnipsWeatherConditions, mappings
import random
from utils import _convert_to_unix_case
from weather import WeatherConditions


class WeatherConditionDescriptor(object):
    """
    A utility class that describes description sentences for WeatherCondition.
    """

    def __init__(self, key):
        self.value = key

    descriptions = {
        WeatherConditions.THUNDERSTORM: {
            "en_US": ["Thunderstorms are expected", "expect thunderstorms"],
            "fr_FR": ["de l'orage et des éclair sont prévus"],
            "es_ES": ["Se esperan tormentas"],
        },
        WeatherConditions.DRIZZLE: {
            "en_US": ["drizzle are expected", "expect drizzle"],
            "fr_FR": ["prévoir de la bruine"],
            "es_ES": ["Se espera granizo"],
        },
        WeatherConditions.RAIN: {
            "en_US": ["rain is expected", "it's going to be rainy", "expect rain"],
            "fr_FR": ["il va pleuvoir", "il pleuvra", "le temps sera pluvieux"],
            "es_ES": ["Se esperan lluvias"],
        },
        WeatherConditions.SNOW: {
            "en_US": ["snow is expected", "it's going to snow", "expect snow"],
            "fr_FR": ["il neigera", "il va neiger", "le temps sera neigeux"],
            "es_ES": ["Se esperan nevadas"],
        },
        WeatherConditions.FOG: {
            "en_US": ["fog is expected", "it's going to be foggy", "expect fog"],
            "fr_FR": ["Il y aura du brouillard"],
            "es_ES": ["Se espera niebla"],
        },
        WeatherConditions.SUN: {
            "en_US": ["sun is expected", "it's going to be sunny", "the sun will shine"],
            "fr_FR": ["le temps sera ensoleillé"],
            "es_ES": ["Se espera sol", "El sol brillará"],
        },
        WeatherConditions.CLOUDS: {
            "en_US": ["it's going to be cloudy", "expect clouds"],
            "fr_FR": ["le temps sera nuageux"],
            "es_ES": ["Se esperan nubes", "El cielo estará nublado"],
        },
        WeatherConditions.STORM: {
            "en_US": ["storms are expected", "it's going to be stormy", "expect storms"],
            "fr_FR": ["il y aura de l'orage"],
            "es_ES": ["Se esperan tormentas"],
        },
        WeatherConditions.HUMID: {
            "en_US": ["humidity is expected", "it's going to be humid"],
            "fr_FR": ["le temps sera humide"],
            "es_ES": ["La humedad será elevada"],
        },
        WeatherConditions.WIND: {
            "en_US": ["wind is expected", "it's going to be windy", "expect wind"],
            "fr_FR": ["s'attendre à du vent"],
            "es_ES": ["Se espera un tiempo ventoso"],
        },
        WeatherConditions.UNKNOWN: {
            "en_US": ["I don't know how to describe the weather"],
            "fr_FR": ["Je ne peux pas décrire la météo"],
            "es_ES": ["No puedo decirte el tiempo que hará"],
        },
    }

    def describe(self, locale):
        return random.choice(self.descriptions[self.value][locale])


class SnipsToWeatherConditionMapper(object):
    mappings = {
        SnipsWeatherConditions.HUMID: WeatherConditions.HUMID,
        SnipsWeatherConditions.BLIZZARD: WeatherConditions.FOG,
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
        SnipsWeatherConditions.WIND: WeatherConditions.WIND,
        SnipsWeatherConditions.TRENCH_COAT: WeatherConditions.RAIN,
        # TODO REMOVE WHEN INTENT 'ITEM' WILL BE INDEPENDENTLY MANAGED
        SnipsWeatherConditions.PARKA: WeatherConditions.RAIN,
        SnipsWeatherConditions.CARDIGAN: WeatherConditions.RAIN,
        SnipsWeatherConditions.SUMMER_CLOTHING: WeatherConditions.SUN,
        SnipsWeatherConditions.GAMP: WeatherConditions.RAIN,
        SnipsWeatherConditions.BROLLY: WeatherConditions.RAIN,
        SnipsWeatherConditions.SUNSHADE: WeatherConditions.SUN,
        SnipsWeatherConditions.PARASOL: WeatherConditions.SUN,
        SnipsWeatherConditions.UMBRELLA: WeatherConditions.RAIN,
        SnipsWeatherConditions.OPEN_TOED_SHOES: WeatherConditions.SUN,
        SnipsWeatherConditions.SHORTS: WeatherConditions.SUN,
        SnipsWeatherConditions.SKIRT: WeatherConditions.SUN,
        SnipsWeatherConditions.WARM_JUMPER: WeatherConditions.SNOW,
        SnipsWeatherConditions.WARM_SOCKS: WeatherConditions.SNOW,
        SnipsWeatherConditions.WARM_SWEATER: WeatherConditions.SNOW,
        SnipsWeatherConditions.SCARF: WeatherConditions.SNOW,
        SnipsWeatherConditions.STRAW_HAT: WeatherConditions.SUN,
        SnipsWeatherConditions.HAT: WeatherConditions.SUN,
        SnipsWeatherConditions.SUNBLOCK: WeatherConditions.SUN,
        SnipsWeatherConditions.SUNSCREEN: WeatherConditions.SUN,
        SnipsWeatherConditions.SUN_CREAM: WeatherConditions.SUN,
        SnipsWeatherConditions.WOOLEN_SWEATER: WeatherConditions.SNOW,
        SnipsWeatherConditions.WOOLEN_JUMPER: WeatherConditions.SNOW,
        SnipsWeatherConditions.WOOLEN_SOCKS: WeatherConditions.SNOW,
        SnipsWeatherConditions.WOOLEN_TIGHTS: WeatherConditions.SNOW,
        SnipsWeatherConditions.SLEEVELESS_SUNDRESS: WeatherConditions.SUN,
        SnipsWeatherConditions.SUNDRESS: WeatherConditions.SUN,
        SnipsWeatherConditions.CHUNKY_SWEATER: WeatherConditions.CLOUDS,
        SnipsWeatherConditions.SUNGLASSES: WeatherConditions.SUN,
        SnipsWeatherConditions.RAINCOAT: WeatherConditions.RAIN

    }

    def __init__(self, key=None):
        self.value = None
        if key:
            if type(key) is SnipsWeatherConditions:
                self.value = key
            elif type(key) is int:
                try:
                    self.value = SnipsWeatherConditions(key)
                except:
                    pass
            elif type(key) is str:
                if key in SnipsWeatherConditions.__members__:
                    self.value = SnipsWeatherConditions[key]

    def fuzzy_matching(self, locale, condition_name):
        self.value = SlotValueResolver().fuzzy_match(locale, condition_name)
        return self

    def resolve(self):
        """
        Resolves a SnipsWeatherCondition to a WeatherCondition
        :return: a WeatherCondition
        :rtype: WeatherCondition
        """
        if self.value is None: return WeatherConditionDescriptor(WeatherConditions.UNKNOWN)
        return WeatherConditionDescriptor(self.mappings[self.value])

class SlotValueResolver(object):
    def normalize_input(self, input_string):
        return input_string.lower().strip()

    def fuzzy_match(self, locale, condition_name):
        condition_name = self.normalize_input(condition_name)
        conditions_candidates = self.get_condition_candidates(locale, condition_name)

        sorted_candidates = sorted(conditions_candidates.items(),
                                   cmp=lambda x, y: WagnerFischer(condition_name, x[1]).cost - WagnerFischer(condition_name, y[1]).cost)
        return sorted_candidates[0][0]

    def get_condition_candidates(self, locale, condition_name):
        return {condition: min(mappings[condition][locale], key=lambda s:  WagnerFischer(condition_name, s).cost) for
                condition in list(SnipsWeatherConditions)}


if __name__ == "__main__":
    print SlotValueResolver().fuzzy_match("fr_FR", u'HUMID')
