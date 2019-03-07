# -*- coding: utf-8 -*-
import datetime
import json
import requests
from weather_provider import WeatherProvider, WeatherProviderError, WeatherProviderConnectivityError, WeatherProviderInvalidAPIKey
from enum import Enum
from snipsowm.utils import _convert_to_unix_case
from snipsowm.weather import WeatherConditions
from snipsowm.weather_condition import WeatherConditionDescriptor

class OWMWeatherConditions(Enum):
    THUNDERSTORM_WITH_LIGHT_RAIN = 200
    THUNDERSTORM_WITH_RAIN = 201
    THUNDERSTORM_WITH_HEAVY_RAIN = 202
    LIGHT_THUNDERSTORM = 210
    THUNDERSTORM = 211
    HEAVY_THUNDERSTORM = 212
    RAGGED_THUNDERSTORM = 221
    THUNDERSTORM_WITH_LIGHT_DRIZZLE = 230
    THUNDERSTORM_WITH_DRIZZLE = 231
    THUNDERSTORM_WITH_HEAVY_DRIZZLE = 232
    LIGHT_INTENSITY_DRIZZLE = 300
    DRIZZLE = 301
    HEAVY_INTENSITY_DRIZZLE = 302
    LIGHT_INTENSITY_DRIZZLE_RAIN = 310
    DRIZZLE_RAIN = 311
    HEAVY_INTENSITY_DRIZZLE_RAIN = 312
    SHOWER_RAIN_AND_DRIZZLE = 313
    HEAVY_SHOWER_RAIN_AND_DRIZZLE = 314
    SHOWER_DRIZZLE = 321
    LIGHT_RAIN = 500
    MODERATE_RAIN = 501
    HEAVY_INTENSITY_RAIN = 502
    VERY_HEAVY_RAIN = 503
    EXTREME_RAIN = 504
    FREEZING_RAIN = 511
    LIGHT_INTENSITY_SHOWER_RAIN = 520
    SHOWER_RAIN = 521
    HEAVY_INTENSITY_SHOWER_RAIN = 522
    RAGGED_SHOWER_RAIN = 531
    LIGHT_SNOW = 600
    SNOW = 601
    HEAVY_SNOW = 602
    SLEET = 611
    SHOWER_SLEET = 612
    LIGHT_RAIN_AND_SNOW = 615
    RAIN_AND_SNOW = 616
    LIGHT_SHOWER_SNOW = 620
    SHOWER_SNOW = 621
    HEAVY_SHOWER_SNOW = 622
    MIST = 701
    SMOKE = 711
    HAZE = 721
    SAND_DUST_WHIRLS = 731
    FOG = 741
    SAND = 751
    DUST = 761
    VOLCANIC_ASH = 762
    SQUALLS = 771
    TORNAD = 781
    CLEAR_SKY = 800
    FEW_CLOUDS = 801
    SCATTERED_CLOUDS = 802
    BROKEN_CLOUDS = 803
    OVERCAST_CLOUDS = 804
    TORNADO = 900 
    TROPICAL_STORM = 901 
    HURRICANE = 902 
    COLD = 903 
    HOT = 904 
    WINDY = 905 
    HAIL = 906 

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


class OWMWeatherProvider(WeatherProvider):
    API_WEATHER_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
    API_FORECAST_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
    OWM_MAX_FORECAST_DAYS = 15

    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_weather(self, location):
        """Perform the API request.

        :param location: The location of the forecast, e.g. 'Paris,fr' or
                         'Eiffel Tower'
        """
        url = "{}?APPID={}&q={}&units=metric".format(self.API_WEATHER_ENDPOINT,
                                                     self.api_key,
                                                     location)
        r = requests.get(url)
        response = json.loads(r.text)

        if response['cod'] == 404:
            raise OpenWeatherMapQueryError(response['message'])

        if response['cod'] == 401:
            raise OpenWeatherMapAPIKeyError(response['message'])

        try:
            description = response["weather"][0]["id"]
        except (KeyError, IndexError, UnicodeEncodeError):
            description = None
        try:
            temperature = int(float(response["main"]["temp"]))
        except KeyError:
            temperature = None
        return description, temperature

    def get_forecast_weather(self, location, datetime):
        """
        Perform the API request.
        :param location: The location of the asked forecast
        :type location: string
        :param datetime: The date and time of the requested forecast
        :type datetime: datetime
        :return: description of the asked weather and the temperature
        :rtype: (str, int)
        """
        url = "{}?APPID={}&q={}&units=metric".format(self.API_FORECAST_ENDPOINT,
                                                     self.api_key,
                                                     location)
        r = requests.get(url)
        response = json.loads(r.text)

        if response['cod'] == 404:
            raise OpenWeatherMapQueryError(response['message'])

        if response['cod'] == 401:
            raise OpenWeatherMapAPIKeyError(response['message'])

        response = self._getTopicalInfos(response, datetime)

        try:
            description = response["weather"][0]["id"]
        except (KeyError, IndexError, UnicodeEncodeError):
            description = None
        try:
            temperature = int(float(response["main"]["temp"]))
        except KeyError:
            temperature = None
        return description, temperature

    def get_weather(self, location, datetime=None):
        if datetime:
            self.check_owm_forecast_limit(datetime)
            return self.get_forecast_weather(location, datetime)
        else:
            return self.get_current_weather(location)

    def map_WeatherCondition(self, object):
        return OWMToWeatherConditionMapper(object).resolve()

    def check_owm_forecast_limit(self, dt):
        """

        :param datetime:
        :return:bool
        """
        now_date = datetime.datetime.now()
        if dt < now_date or (dt - now_date).days >= self.OWM_MAX_FORECAST_DAYS:
            raise OpenWeatherMapMaxDaysForecastError(
                "OpenWeather map day forecast limit exceed. Can't get forecast for more than {} days".format(
                    OWMWeatherProvider.OWM_MAX_FORECAST_DAYS))

    def _getTopicalInfos(self, response, date_time):
        delta = date_time - datetime.datetime.strptime(response["list"][0]['dt_txt'], "%Y-%m-%d %H:%M:%S")
        delta = abs(delta)
        result = {}

        for time_interval in response["list"]:
            current_time = datetime.datetime.strptime(time_interval['dt_txt'], "%Y-%m-%d %H:%M:%S")
            current_delta = date_time - current_time
            current_delta = abs(current_delta)
            if delta > current_delta:
                delta = current_delta
                result = time_interval

        return result


class OpenWeatherMapError(WeatherProviderError):
    """Basic exception for errors raised by OWM"""
    pass


class OpenWeatherMapAPIKeyError(WeatherProviderInvalidAPIKey):
    """Exception raised when the wrong API key is provided"""
    pass


class OpenWeatherMapQueryError(OpenWeatherMapError):
    """Exception for 404 errors raised by OWM"""
    pass


class OpenWeatherMapMaxDaysForecastError(OpenWeatherMapError):
    """Exception raised by OWM when a forecast for more than OWMWeatherProvider.OWM_MAX_FORECAST_DAYS days is asked"""
    pass
