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
        'en_US': [u'humid'],
        'es_ES': [u'húmedo'],
        'de_DE': [u'feucht']
    },
    SnipsWeatherConditions.BLIZZARD: {
        'fr_FR': [u'blizzard'],
        'en_US': [u'blizzard'],
        'es_ES': [u'ventisca'],
        'de_DE': [u'Schneesturm']
    },
    SnipsWeatherConditions.SNOWFALL: {
        'fr_FR': [u'chutes de neige'],
        'en_US': [u'snowfall'],
        'es_ES': [u'nieve'],
        'de_DE': [u'Schneefall']
    },
    SnipsWeatherConditions.WINDY: {
        'fr_FR': [u'venteux'],
        'en_US': [u'windy'],
        'es_ES': [u'viento'],
        'de_DE': [u'windig']
    },
    SnipsWeatherConditions.CLOUD: {
        'fr_FR': [u'nuage', u'nuages'],
        'en_US': [u'cloud', u'clouds'],
        'es_ES': [u'nuboso'],
        'de_DE': [u'wolkig', u'bewölkt']
    },
    SnipsWeatherConditions.RAINY: {
        'fr_FR': [u'pluvieux'],
        'en_US': [u'rainy'],
        'es_ES': [u'lluvioso'],
        'de_DE': [u'regnerisch']
    },
    SnipsWeatherConditions.STORMY: {
        'fr_FR': [u'orageux'],
        'en_US': [u'stormy'],
        'es_ES': [u'tormentoso'],
        'de_DE': [u'stürmisch']
    },
    SnipsWeatherConditions.SUN: {
        'fr_FR': [u'soleil'],
        'en_US': [u'sun'],
        'es_ES': [u'soleado'],
        'de_DE': [u'Sonne']
    },
    SnipsWeatherConditions.SNOW: {
        'fr_FR': [u'neige', u'neiger', u'neigera'],
        'en_US': [u'snow'],
        'es_ES': [u'nieve'],
        'de_DE': [u'Schnee']
    },
    SnipsWeatherConditions.FOG: {
        'fr_FR': [u'brouillard'],
        'en_US': [u'fog'],
        'es_ES': [u'niebla'],
        'de_DE': [u'Nebel']
    }, SnipsWeatherConditions.DEPRESSION: {
        'fr_FR': [u'dépression'],
        'en_US': [u'depression'],
        'es_ES': [u'depresión'],
        'de_DE': [u'Tief']
    },
    SnipsWeatherConditions.STORM: {
        'fr_FR': [u'tempête'],
        'en_US': [u'storm'],
        'es_ES': [u'tormenta'],
        'de_DE': [u'Sturm']
    },
    SnipsWeatherConditions.RAINFALL: {
        'fr_FR': [u'précipitations'],
        'en_US': [u'rainfall'],
        'es_ES': [u'precipitaciones'],
        'de_DE': [u'Niederschlag']
    },
    SnipsWeatherConditions.SNOWY: {
        'fr_FR': [u'neigeux'],
        'en_US': [u'snowy'],
        'es_ES': [u'nevada'],
        'de_DE': [u'verschneit']
    },
    SnipsWeatherConditions.SUNNY: {
        'fr_FR': [u'ensoleillé'],
        'en_US': [u'sunny'],
        'es_ES': [u'soleado'],
        'de_DE': [u'sonnig']
    },
    SnipsWeatherConditions.RAIN: {
        'fr_FR': [u'pluie'],
        'en_US': [u'rain'],
        'es_ES': [u'lluvia'],
        'de_DE': [u'Regen']
    },
    SnipsWeatherConditions.HAIL: {
        'fr_FR': [u'grêle'],
        'en_US': [u'hail'],
        'es_ES': [u'granizo'],
        'de_DE': [u'Hagel']
    },
    SnipsWeatherConditions.FOGGY: {
        'fr_FR': [u'brumeux'],
        'en_US': [u'foggy'],
        'es_ES': [u'nebuloso'],
        'de_DE': [u'neblig']
    },
    SnipsWeatherConditions.OVERCAST: {
        'fr_FR': [u'couvert'],
        'en_US': [u'overcast'],
        'es_ES': [u'cubierto'],
        'de_DE': [u'bewölkt']
    },
    SnipsWeatherConditions.CLOUDY: {
        'fr_FR': [u'nuageux'],
        'en_US': [u'cloudy'],
        'es_ES': [u'nublado'],
        'de_DE': [u'wolkig']
    },
    SnipsWeatherConditions.HUMIDITY: {
        'fr_FR': [u'humidité'],
        'en_US': [u'humidity'],
        'es_ES': [u'humedad'],
        'de_DE': [u'Luftfeuchtigkeit']
    }, SnipsWeatherConditions.SNOWSTORM: {
        'fr_FR': [u'tempête de neige'],
        'en_US': [u'snowstorm'],
        'es_ES': [u'tormenta de nieve'],
        'de_DE': [u'Schneesturm']
    },
    SnipsWeatherConditions.WIND: {
        'fr_FR': [u'vent'],
        'en_US': [u'wind'],
        'es_ES': [u'viento'],
        'de_DE': [u'Wind']
    },
    SnipsWeatherConditions.TRENCH_COAT: {
        'fr_FR': [u'trench'],
        'en_US': [u'trench coat'],
        'es_ES': [u'gabardina'],
        'de_DE': [u'Regenmantel']
    },
    SnipsWeatherConditions.PARKA: {
        'fr_FR': [u'parka'],
        'en_US': [u'parka'],
        'es_ES': [u'anorak'],
        'de_DE': [u'Anorak']
    },
    SnipsWeatherConditions.CARDIGAN: {
        'fr_FR': [u'cardigan'],
        'en_US': [u'cardigan'],
        'es_ES': [u'chaqueta'],
        'de_DE': [u'Strickjacke']
    },
    SnipsWeatherConditions.SUMMER_CLOTHING: {
        'fr_FR': [u'légé'],
        'en_US': [u'summer clothing'],
        'es_ES': [u'ropa de verano'],
        'de_DE': [u'Sommerkleidung']
    },
    SnipsWeatherConditions.GAMP: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'gamp'],
        'es_ES': [u'paraguas'],
        'de_DE': [u'Regenschirm']
    },
    SnipsWeatherConditions.BROLLY: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'brolly'],
        'es_ES': [u'paraguas'],
        'de_DE': [u'Regenschirm']
    },
    SnipsWeatherConditions.SUNSHADE: {
        'fr_FR': [u'parasol'],
        'en_US': [u'sunshade'],
        'es_ES': [u'sombrilla'],
        'de_DE': [u'Sonnenschirm']
    },
    SnipsWeatherConditions.PARASOL: {
        'fr_FR': [u'parasol'],
        'en_US': [u'parasol'],
        'es_ES': [u'sombrilla'],
        'de_DE': [u'Sonnenshirm']
    },
    SnipsWeatherConditions.UMBRELLA: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'umbrella'],
        'es_ES': [u'paraguas'],
        'de_DE': [u'Schirm']
    }, SnipsWeatherConditions.OPEN_TOED_SHOES: {
        'fr_FR': [u'sandales'],
        'en_US': [u'open toed shoes'],
        'es_ES': [u'sandalias'],
        'de_DE': [u'Sandalen']
    },
    SnipsWeatherConditions.SHORTS: {
        'fr_FR': [u'short'],
        'en_US': [u'shorts'],
        'es_ES': [u'pantalones cortos'],
        'de_DE': [u'kurze Hose']
    },
    SnipsWeatherConditions.SKIRT: {
        'fr_FR': [u'jupe'],
        'en_US': [u'skirt'],
        'es_ES': [u'falda'],
        'de_DE': [u'Rock']
    },
    SnipsWeatherConditions.WARM_JUMPER: {
        'fr_FR': [u'jupe courte'],
        'en_US': [u'warm jumper'],
        'es_ES': [u'jersey cálido'],
        'de_DE': [u'warmen Pulli']
    },
    SnipsWeatherConditions.WARM_SOCKS: {
        'fr_FR': [u'chausettes chaudes'],
        'en_US': [u'warm socks'],
        'es_ES': [u'calcetines cálidos'],
        'de_DE': [u'warme Socken']
    },
    SnipsWeatherConditions.WARM_SWEATER: {
        'fr_FR': [u'pull'],
        'en_US': [u'warm sweater'],
        'es_ES': [u'jersey cálido'],
        'de_DE': [u'warmen Pullover']
    },
    SnipsWeatherConditions.SCARF: {
        'fr_FR': [u'écharpe'],
        'en_US': [u'scarf'],
        'es_ES': [u'bufanda'],
        'de_DE': [u'Schal']
    },
    SnipsWeatherConditions.STRAW_HAT: {
        'fr_FR': [u'chapeau de paille'],
        'en_US': [u'straw hat'],
        'es_ES': [u'sombero de paja'],
        'de_DE': [u'Strohhut']
    },
    SnipsWeatherConditions.HAT: {
        'fr_FR': [u'chapeau'],
        'en_US': [u'hat'],
        'es_ES': [u'sombrero'],
        'de_DE': [u'Hut']
    },
    SnipsWeatherConditions.SUNBLOCK: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sunblock'],
        'es_ES': [u'crema solar'],
        'de_DE': [u'Sonnencreme']
    },
    SnipsWeatherConditions.SUNSCREEN: {
        'fr_FR': [u'écran solaire'],
        'en_US': [u'sunscreen'],
        'es_ES': [u'protector solar'],
        'de_DE': [u'Sonnencreme']
    }, SnipsWeatherConditions.SUN_CREAM: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sun cream'],
        'es_ES': [u'crema solar'],
        'de_DE': [u'Sonnencreme']
    },
    SnipsWeatherConditions.WOOLEN_SWEATER: {
        'fr_FR': [u'pull en laine'],
        'en_US': [u'woolen sweater'],
        'es_ES': [u'jersey de lana'],
        'de_DE': [u'Wollpullover']
    },
    SnipsWeatherConditions.WOOLEN_JUMPER: {
        'fr_FR': [u'pull en laine'],
        'en_US': [u'woolen jumper'],
        'es_ES': [u'jersey de lana'],
        'de_DE': [u'Wollpullover']
    },
    SnipsWeatherConditions.WOOLEN_TIGHTS: {
        'fr_FR': [u'collants en laine'],
        'en_US': [u'woolen tights'],
        'es_ES': [u'medias de lana'],
        'de_DE': [u'Wollstrumpfhose']
    },
    SnipsWeatherConditions.SLEEVELESS_SUNDRESS: {
        'fr_FR': [u'robe d\'été'],
        'en_US': [u'sleeveless sundress'],
        'es_ES': [u'vestido sin mangas'],
        'de_DE': [u'ärmelloses Sommerkleid']
    },
    SnipsWeatherConditions.SUNDRESS: {
        'fr_FR': [u'robe d\'été'],
        'en_US': [u'sundress'],
        'es_ES': [u'vestido de verano'],
        'de_DE': [u'Sommerkleid']
    },
    SnipsWeatherConditions.CHUNKY_SWEATER: {
        'fr_FR': [u'gros pull'],
        'en_US': [u'chunky sweater'],
        'es_ES': [u'jersey grueso'],
        'de_DE': [u'dicken Pullover']
    },
    SnipsWeatherConditions.SUNGLASSES: {
        'fr_FR': [u'lunettes de soleil'],
        'en_US': [u'sunglasses'],
        'es_ES': [u'gafas de sol'],
        'de_DE': [u'Sonnenbrille']
    },
    SnipsWeatherConditions.RAINCOAT: {
        'fr_FR': [u'manteau pour la pluie'],
        'en_US': [u'raincoat'],
        'es_ES': [u'impermeable'],
        'de_DE': [u'Regenmantel']
    },
    SnipsWeatherConditions.WOOLEN_SOCKS: {
        'fr_FR': [u'chaussettes en laine'],
        'en_US': [u'woolen socks'],
        'es_ES': [u'calcetines de lana'],
        'de_DE': [u'Wollsocken']
    }
}
