# Snips Weather Skill

## Installation

Install the required dependencies:

```sh
$ sudo apt-get install git python-pip
$ sudo easy_install --upgrade pip
$ sudo pip install paho-mqtt requests==2.6.0
```

## Running

Start the skill server by running the following command, providing your OpenWeatherMap API key ((generate one here)[]) as well as the default location for weather forecasts:

```sh
$ python server.py --owm_api_key=YOUR_API_KEY --default_location=Paris,fr
```