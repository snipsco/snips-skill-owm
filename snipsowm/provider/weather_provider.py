# -*- coding: utf-8 -*-

import abc

class WeatherProvider(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_current_weather(self):
        pass
    @abc.abstractmethod
    def get_forecast_weather(self):
        pass

    @abc.abstractmethod
    def get_weather(self):
        pass



class WeatherProviderError(Exception):
    pass

class WeatherProviderConnectivityError(Exception):
    pass

