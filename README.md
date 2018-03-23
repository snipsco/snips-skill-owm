# OpenWeatherMap skill for Snips

[![Build Status](https://travis-ci.org/snipsco/snips-skill-owm.svg)](https://travis-ci.org/snipsco/snips-skill-owm)
[![PyPi](https://img.shields.io/pypi/v/snips-skill-owm.svg)](https://pypi.python.org/pypi/snips-skill-owm)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/snipsco/snips-skill-owm/master/LICENSE.txt)

## Installation
------------

The skill is on [PyPI](https://pypi.python.org/pypi/snips-skill-owm), so you can just install it with [pip](http://www.pip-installer.org):

```sh
$ pip install snipsowm
```

## Locale

To have the skills properly working, you **need** to generate locales for your languages.  So far the supported locales are:

- 🇺🇸 `en_US`
- 🇫🇷 `fr_FR`

You can generate them with `sudo raspi-config`. Going in the `Localisation Options` submenu, then in the `Change Locale` submenu, and selecting the locales you want to support. For instance, select `en_US UTF-8` if you want support for English. 

## Usage

### Snips Skills Manager

It is recommended that you use this skill with the [Snips Skills Manager](https://github.com/snipsco/snipsskills). Simply add the following section to your [Snipsfile](https://github.com/snipsco/snipsskills/wiki/The-Snipsfile):

```sh
locale: <Desired Locale>
skills:
- package_name: snipsowm
  class_name: SnipsOWM
  pip: snipsowm
  default_location: "Paris,fr"
  params:
    api_key: <YOUR API KEY>
    default_location: France
```

## Contributing

Please see the [Contribution Guidelines](https://github.com/snipsco/snips-skill-owm/blob/master/CONTRIBUTING.md).

## Copyright

This skill is provided by [Snips](https://www.snips.ai) as Open Source software. See [LICENSE.txt](https://github.com/snipsco/snips-skill-owm/blob/master/LICENSE.txt) for more information.
