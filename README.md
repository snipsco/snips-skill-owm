OpenWeatherMap skill for Snips
===

[![Build Status](https://travis-ci.org/snipsco/snips-skill-weather-owm.svg)](https://travis-ci.org/snipsco/snips-skill-weather-owm)

## Installation

Install dependencies

```sh
$ python setup.py install --user
```

## Running

Start the skill server by running the following command, providing your OpenWeatherMap API key ((generate one here)[]) as well as the default location for weather forecasts:

```sh
$ python server.py --owm_api_key=YOUR_API_KEY --default_location=Paris,fr
```
