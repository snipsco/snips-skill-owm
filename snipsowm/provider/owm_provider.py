# -*- coding: utf-8 -*-
import datetime
import json
import requests
from weather_provider import WeatherProvider, WeatherProviderError, WeatherProviderConnectivityError

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
        return (description, temperature)

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
        return (description, temperature)

    def get_weather(self, location, datetime=None):
        if datetime:
            self.check_owm_forecast_limit(datetime)
            return self.get_forecast_weather(location, datetime)
        else:
            return self.get_current_weather(location)

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

class OpenWeatherMapAPIKeyError(WeatherProviderConnectivityError):
    """Exception raised when the wrong API key is provided"""
    pass

class OpenWeatherMapQueryError(OpenWeatherMapError):
    """Exception for 404 errors raised by OWM"""
    pass

class OpenWeatherMapMaxDaysForecastError(OpenWeatherMapError):
    """Exception raised by OWM when a forecast for more than OWMWeatherProvider.OWM_MAX_FORECAST_DAYS days is asked"""
    pass
