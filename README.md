# Snips Weather Skill

## Installation

Make sure `pip` is available on your system:

```sh
$ sudo apt-get install git python-pip
$ sudo easy_install --upgrade pip
```

Then install the dependencies from `requirements.txt`:

```sh
$ sudo -H pip install -r requirements.txt
```

## Configuration

## Running

Start the skill server by running the following command, providing your OpenWeatherMap API key ((generate one here)[]) as well as the default location for weather forecasts:

```sh
$ python server.py --owm_api_key=YOUR_API_KEY --default_location=Paris,fr
```