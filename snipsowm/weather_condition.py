# -*- coding: utf-8 -*-
from wagnerfischerpp import WagnerFischer
from owm import OWMWeatherConditions
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
            "de_DE": ["Es werden Gewitter erwartet", "Es ist mit Gewitter zu rechnen"],
        },
        WeatherConditions.DRIZZLE: {
            "en_US": ["drizzle are expected", "expect drizzle"],
            "fr_FR": ["prévoir de la bruine"],
            "es_ES": ["Se espera granizo"],
            "de_DE": ["Es wird Nieselregen erwartet", "Es ist mit Nieselregen zu rechnen"],
        },
        WeatherConditions.RAIN: {
            "en_US": ["rain is expected", "it's going to be rainy", "expect rain"],
            "fr_FR": ["il va pleuvoir", "il pleuvra", "le temps sera pluvieux"],
            "es_ES": ["Se esperan lluvias"],
            "de_DE": ["Es wird Regen erwartet", "Es ist mit Regen zu rechnen"],
        },
        WeatherConditions.SNOW: {
            "en_US": ["snow is expected", "it's going to snow", "expect snow"],
            "fr_FR": ["il neigera", "il va neiger", "le temps sera neigeux"],
            "es_ES": ["Se esperan nevadas"],
            "de_DE": ["Es wird Schnee erwartet", "Es ist mit Schnee zu rechnen"],
        },
        WeatherConditions.FOG: {
            "en_US": ["fog is expected", "it's going to be foggy", "expect fog"],
            "fr_FR": ["Il y aura du brouillard"],
            "es_ES": ["Se espera niebla"],
            "de_DE": ["Es wird Nebel erwartet", "Es ist mit Nebel zu rechnen"],
        },
        WeatherConditions.SUN: {
            "en_US": ["sun is expected", "it's going to be sunny", "the sun will shine"],
            "fr_FR": ["le temps sera ensoleillé"],
            "es_ES": ["Se espera sol", "El sol brillará"],
            "de_DE": ["Es wird sonnig sein", "Es ist mit Sonne zu rechnen"],
        },
        WeatherConditions.CLOUDS: {
            "en_US": ["it's going to be cloudy", "expect clouds"],
            "fr_FR": ["le temps sera nuageux"],
            "es_ES": ["Se esperan nubes", "El cielo estará nublado"],
            "de_DE": ["Es wird wolkig sein", "Es ist mit bewölkung zu rechnen"],
        },
        WeatherConditions.STORM: {
            "en_US": ["storms are expected", "it's going to be stormy", "expect storms"],
            "fr_FR": ["il y aura de l'orage"],
            "es_ES": ["Se esperan tormentas"],
            "de_DE": ["Es wird Sturm erwartet", "Es ist mit Sturm zu rechnen"],
        },
        WeatherConditions.HUMID: {
            "en_US": ["humidity is expected", "it's going to be humid"],
            "fr_FR": ["le temps sera humide"],
            "es_ES": ["La humedad será elevada"],
            "de_DE": ["Es kann mit Nässe gerechnet werden"],
        },
        WeatherConditions.WIND: {
            "en_US": ["wind is expected", "it's going to be windy", "expect wind"],
            "fr_FR": ["s'attendre à du vent"],
            "es_ES": ["Se espera un tiempo ventoso"],
            "de_DE": ["Es wird windig", "Es kann mit Wind gerechnet werden"],
        },
        WeatherConditions.UNKNOWN: {
            "en_US": ["I don't know how to describe the weather"],
            "fr_FR": ["Je ne peux pas décrire la météo"],
            "es_ES": ["No puedo decirte el tiempo que hará"],
            "de_DE": ["Ich weis nicht wie ich das Wetter beschreiben soll"],
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


class OWMToWeatherConditionMapper(object):
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
        OWMWeatherConditions.OVERCAST_CLOUDS: WeatherConditions.CLOUDS,
        OWMWeatherConditions.CLEAR_SKY: WeatherConditions.SUN,
        OWMWeatherConditions.TORNADO: WeatherConditions.STORM,
        OWMWeatherConditions.TROPICAL_STORM: WeatherConditions.STORM,
        OWMWeatherConditions.HURRICANE: WeatherConditions.STORM,
        OWMWeatherConditions.COLD: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.HOT: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.WINDY: WeatherConditions.UNKNOWN,
        OWMWeatherConditions.HAIL: WeatherConditions.UNKNOWN
    }

    def __init__(self, key):
        self.value = None
        if type(key) is OWMWeatherConditions:
            self.value = key
        elif type(key) is int:
            try:
                self.value = OWMWeatherConditions(key)
            except:
                pass
        elif type(key) is str:
            key = _convert_to_unix_case(key)
            if key in OWMWeatherConditions.__members__:
                self.value = OWMWeatherConditions[key]

    def resolve(self):
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