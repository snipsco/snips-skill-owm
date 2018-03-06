from unittest import TestCase

import datetime
from snipsowm.provider import owm_provider


class TestGetWeather(TestCase):
    def setUp(self):
        self.api_key = "dummykey"
        self.provider = owm_provider.OWMWeatherProvider(self.api_key)

    def test_get_weather_owm_forecast_limit_low(self):
        now_date = datetime.datetime.now()
        now_date_minus_1_day = now_date + datetime.timedelta(days=-1)
        self.assertRaises(owm_provider.OpenWeatherMapMaxDaysForecastError, self.provider.check_owm_forecast_limit,
                          now_date_minus_1_day)

    def test_get_weather_owm_forecast_limit_high(self):
        now_date = datetime.datetime.now()
        now_date_minus_15_day = now_date + datetime.timedelta(
            days=owm_provider.OWMWeatherProvider.OWM_MAX_FORECAST_DAYS + 1)
        self.assertRaises(owm_provider.OpenWeatherMapMaxDaysForecastError, self.provider.check_owm_forecast_limit,
                          now_date_minus_15_day)

