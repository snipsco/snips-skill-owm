# OpenWeatherMap skill for Snips

## Installation

Install dependencies
```sh
$ python setup.py install --user
```

## Configuration

## Running

Start the skill server by running the following command, providing your OpenWeatherMap API key ((generate one here)[]) as well as the default location for weather forecasts:

```sh
$ python server.py --owm_api_key=YOUR_API_KEY --default_location=Paris,fr
```




install:
	sudo apt-get install git python-pip
	sudo easy_install --upgrade pip
	pip install pycodestyle
	pip install autopep8
	python setup.py install --user

format:
	sudo autopep8 --in-place --recursive .

check-codestyle:
	pycodestyle server.py
	pycodestyle snips_skill_weather_owm/weather.py

test:
	python setup.py test