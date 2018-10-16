# OpenWeatherMap action for Snips

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/snipsco/snips-skill-owm/master/LICENSE.txt)

## Installation with Sam

The easiest way to use this Action is to install it with [Sam](https://snips.gitbook.io/getting-started/installation)

`sam install actions -g https://github.com/snipsco/snips-skill-owm.git`

Sam will then ask you for an OpenWeatherMap API key. You can create one by signing up to [OpenWeatherMap](https://openweathermap.org)

The action works with the English Weather skill that you can download on [Snips' console](https://console.snips.ai)

## Locale
> ***BEWARE: Please do not forget that you have to specify one of the following values as the locale setting during the installation. If you install it manually, please do give this setting to `config.ini` -> `locale=`. Otherwise, it will not work as expected.***

To have the skills properly working, you **need** to generate locales for your languages.  So far the supported locales are:

- 🇺🇸 `en_US`
- 🇫🇷 `fr_FR`
- 🇪🇸 `es_ES`

You can generate them with `sudo raspi-config`. Going in the `Localisation Options` submenu, then in the `Change Locale` submenu, and selecting the locales you want to support. For instance, select `en_US UTF-8` if you want support for English. 

## Manual installation

- Clone the repository on your Pi
- Run `setup.sh` (it will create a virtualenv, install the dependencies in it and rename config.ini.default to config.ini)
- Provide an OpenWeatherMap API key in the config.ini
- Run `action-owm.py`

## Contributing

Please see the [Contribution Guidelines](https://github.com/snipsco/snips-skill-owm/blob/master/CONTRIBUTING.md).

## Copyright

This action is provided by [Snips](https://www.snips.ai) as Open Source software. See [LICENSE.txt](https://github.com/snipsco/snips-skill-owm/blob/master/LICENSE.txt) for more information.
