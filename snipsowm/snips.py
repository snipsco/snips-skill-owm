# -*- coding: utf-8 -*-
from enum import Enum


class SnipsWeatherConditions(Enum):
    HUMID = 0
    BLIZZARD = 1
    SNOWFALL = 2
    WINDY = 3
    CLOUD = 4
    RAINY = 5
    STORMY = 6
    SUN = 7
    SNOW = 8
    FOG = 9
    DEPRESSION = 10
    STORM = 11
    RAINFALL = 12
    SNOWY = 13
    SUNNY = 14
    RAIN = 15
    HAIL = 16
    FOGGY = 17
    OVERCAST = 18
    CLOUDY = 19
    HUMIDITY = 20
    SNOWSTORM = 21
    WIND = 22
    TRENCH_COAT = 23  # TODO REMOVE WHEN INTENT 'ITEM' WILL BE INDEPENDENTLY MANAGE
    PARKA = 24
    CARDIGAN = 25
    SUMMER_CLOTHING = 26
    GAMP = 27
    BROLLY = 28
    SUNSHADE = 29
    PARASOL = 30
    UMBRELLA = 31
    OPEN_TOED_SHOES = 32
    SHORTS = 33
    SKIRT = 34
    WARM_JUMPER = 35
    WARM_SOCKS = 36
    WARM_SWEATER = 37
    SCARF = 38
    STRAW_HAT = 39
    HAT = 40
    SUNBLOCK = 41
    SUNSCREEN = 42
    SUN_CREAM = 43
    WOOLEN_SWEATER = 44
    WOOLEN_JUMPER = 45
    WOOLEN_SOCKS = 46
    WOOLEN_TIGHTS = 47
    SLEEVELESS_SUNDRESS = 48
    SUNDRESS = 49
    CHUNKY_SWEATER = 50
    SUNGLASSES = 51
    RAINCOAT = 52


mappings = {
    SnipsWeatherConditions.HUMID: {
        'fr_FR': [u'humide'],
        'en_US': [u'humid']
    },
    SnipsWeatherConditions.BLIZZARD: {
        'fr_FR': [u'blizzard'],
        'en_US': [u'blizzard']
    },
    SnipsWeatherConditions.SNOWFALL: {
        'fr_FR': [u'snowfall'],
        'en_US': [u'chutes de neige']
    },
    SnipsWeatherConditions.WINDY: {
        'fr_FR': [u''],
        'en_US': [u'windy']
    },
    SnipsWeatherConditions.CLOUD: {
        'fr_FR': [u'nuage', u'nuages'],
        'en_US': [u'cloud', u'clouds']
    },
    SnipsWeatherConditions.RAINY: {
        'fr_FR': [u'pluvieux'],
        'en_US': [u'rainy']
    },
    SnipsWeatherConditions.STORMY: {
        'fr_FR': [u''],
        'en_US': [u'stormy']
    },
    SnipsWeatherConditions.SUN: {
        'fr_FR': [u'soleil'],
        'en_US': [u'sun']
    },
    SnipsWeatherConditions.SNOW: {
        'fr_FR': [u'neige', u'neiger', u'neigera'],
        'en_US': [u'snow']
    },
    SnipsWeatherConditions.FOG: {
        'fr_FR': [u'brouillard'],
        'en_US': [u'fog']
    }, SnipsWeatherConditions.DEPRESSION: {
        'fr_FR': [u'dépression'],
        'en_US': [u'depression']
    },
    SnipsWeatherConditions.STORM: {
        'fr_FR': [u'tempête'],
        'en_US': [u'storm']
    },
    SnipsWeatherConditions.RAINFALL: {
        'fr_FR': [u'précipitations'],
        'en_US': [u'rainfall']
    },
    SnipsWeatherConditions.SNOWY: {
        'fr_FR': [u'neigeux'],
        'en_US': [u'snowy']
    },
    SnipsWeatherConditions.SUNNY: {
        'fr_FR': [u'ensoleillé'],
        'en_US': [u'sunny']
    },
    SnipsWeatherConditions.RAIN: {
        'fr_FR': [u'pluie'],
        'en_US': [u'rain']
    },
    SnipsWeatherConditions.HAIL: {
        'fr_FR': [u'grêle'],
        'en_US': [u'hail']
    },
    SnipsWeatherConditions.FOGGY: {
        'fr_FR': [u''],
        'en_US': [u'foggy']
    },
    SnipsWeatherConditions.OVERCAST: {
        'fr_FR': [u'couvert'],
        'en_US': [u'overcast']
    },
    SnipsWeatherConditions.CLOUDY: {
        'fr_FR': [u'nuageux'],
        'en_US': [u'cloudy']
    },
    SnipsWeatherConditions.HUMIDITY: {
        'fr_FR': [u'humidité'],
        'en_US': [u'humidity']
    }, SnipsWeatherConditions.SNOWSTORM: {
        'fr_FR': [u'tempête de neige'],
        'en_US': [u'snowstorm']
    },
    SnipsWeatherConditions.WIND: {
        'fr_FR': [u'vent'],
        'en_US': [u'wind']
    },
    SnipsWeatherConditions.TRENCH_COAT: {
        'fr_FR': [u'trench'],
        'en_US': [u'trench coat']
    },
    SnipsWeatherConditions.PARKA: {
        'fr_FR': [u'parka'],
        'en_US': [u'parka']
    },
    SnipsWeatherConditions.CARDIGAN: {
        'fr_FR': [u'cardigan'],
        'en_US': [u'cardigan']
    },
    SnipsWeatherConditions.SUMMER_CLOTHING: {
        'fr_FR': [u''],
        'en_US': [u'summer clothing']
    },
    SnipsWeatherConditions.GAMP: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'gamp']
    },
    SnipsWeatherConditions.BROLLY: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'brolly']
    },
    SnipsWeatherConditions.SUNSHADE: {
        'fr_FR': [u'parasol'],
        'en_US': [u'sunshade']
    },
    SnipsWeatherConditions.PARASOL: {
        'fr_FR': [u'parasol'],
        'en_US': [u'parasol']
    },
    SnipsWeatherConditions.UMBRELLA: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'umbrella']
    }, SnipsWeatherConditions.OPEN_TOED_SHOES: {
        'fr_FR': [u'sandales'],
        'en_US': [u'open toed shoes']
    },
    SnipsWeatherConditions.SHORTS: {
        'fr_FR': [u'short'],
        'en_US': [u'shorts']
    },
    SnipsWeatherConditions.SKIRT: {
        'fr_FR': [u'jupe'],
        'en_US': [u'skirt']
    },
    SnipsWeatherConditions.WARM_JUMPER: {
        'fr_FR': [u''],
        'en_US': [u'warm jumper']
    },
    SnipsWeatherConditions.WARM_SOCKS: {
        'fr_FR': [u'chausettes chaudes'],
        'en_US': [u'warm socks']
    },
    SnipsWeatherConditions.WARM_SWEATER: {
        'fr_FR': [u''],
        'en_US': [u'warm sweater']
    },
    SnipsWeatherConditions.SCARF: {
        'fr_FR': [u'écharpe'],
        'en_US': [u'scarf']
    },
    SnipsWeatherConditions.STRAW_HAT: {
        'fr_FR': [u'chapeau de paille'],
        'en_US': [u'straw hat']
    },
    SnipsWeatherConditions.HAT: {
        'fr_FR': [u'chapeau'],
        'en_US': [u'hat']
    },
    SnipsWeatherConditions.SUNBLOCK: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sunblock']
    },
    SnipsWeatherConditions.SUNSCREEN: {
        'fr_FR': [u'écran solaire'],
        'en_US': [u'sunscreen']
    }, SnipsWeatherConditions.SUN_CREAM: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sun cream']
    },
    SnipsWeatherConditions.WOOLEN_SWEATER: {
        'fr_FR': [u''],
        'en_US': [u'woolen sweater']
    },
    SnipsWeatherConditions.WOOLEN_JUMPER: {
        'fr_FR': [u''],
        'en_US': [u'woolen jumper']
    },
    SnipsWeatherConditions.WOOLEN_TIGHTS: {
        'fr_FR': [u''],
        'en_US': [u'woolen tights']
    },
    SnipsWeatherConditions.SLEEVELESS_SUNDRESS: {
        'fr_FR': [u''],
        'en_US': [u'sleeveless sundress']
    },
    SnipsWeatherConditions.SUNDRESS: {
        'fr_FR': [u''],
        'en_US': [u'sundress']
    },
    SnipsWeatherConditions.CHUNKY_SWEATER: {
        'fr_FR': [u''],
        'en_US': [u'chunky sweater']
    },
    SnipsWeatherConditions.SUNGLASSES: {
        'fr_FR': [u'lunettes de soleil'],
        'en_US': [u'sunglasses']
    },
    SnipsWeatherConditions.RAINCOAT: {
        'fr_FR': [u'manteau pour la pluie'],
        'en_US': [u'raincoat']
    },
    SnipsWeatherConditions.WOOLEN_SOCKS: {
        'fr_FR': [u'chaussettes en laine'],
        'en_US': [u'woolen socks']
    }
}
