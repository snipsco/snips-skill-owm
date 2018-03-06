OpenWeatherMap skill for Snips
==============================

|Build Status| |PyPI| |MIT License|


Installation
------------

The skill is on `PyPI`_, so you can just install it with `pip`_:

.. code-block:: console

    $ pip install snipsowm

Locale
------
To have the skills properly working, you **need** to generate to generate locales for your languages. 
So far the locales that are supported are :

- 🇺🇸 `en_US`
- 🇫🇷 `fr_FR`

You can generate them with `sudo raspi-config`. Going in the `Localisation Options` submenu, then in the `Change Locale` submenu, and selecting the locales you want to support. For instance, select `en_US UTF-8` if you want support for English. 

Usage
-----

Snips Skills Manager
^^^^^^^^^^^^^^^^^^^^

It is recommended that you use this skill with the `Snips Skills Manager <https://github.com/snipsco/snipsskills>`_. Simply add the following section to your `Snipsfile <https://github.com/snipsco/snipsskills/wiki/The-Snipsfile>`_:

.. code-block:: yaml

    locale: <Desired Locale>
    skills:
    - package_name: snipsowm
      class_name: SnipsOWM
      pip: snipsowm
      default_location: "Paris,fr"
      params:
        - api_key: <YOUR API KEY>
          default_location: France
      
Copyright
---------

This skill is provided by `Snips`_ as Open Source software. See `LICENSE.txt`_ for more
information.

.. |Build Status| image:: https://travis-ci.org/snipsco/snips-skill-owm.svg
   :target: https://travis-ci.org/snipsco/snips-skill-owm
   :alt: Build Status
.. |PyPI| image:: https://img.shields.io/pypi/v/snipsowm.svg
   :target: https://pypi.python.org/pypi/snipsowm
   :alt: PyPI
.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/snipsco/snips-skill-owm/master/LICENSE.txt
   :alt: MIT License

.. _`PyPI`: https://pypi.python.org/pypi/snipsowm
.. _`pip`: http://www.pip-installer.org
.. _`OpenWeatherMap`: https://openweathermap.org/
.. _`API key`: https://openweathermap.org/appid#get
.. _`Snips`: https://www.snips.ai
.. _`OpenWeatherMap website`: https://openweathermap.org/api
.. _`LICENSE.txt`: https://github.com/snipsco/snips-skill-owm/blob/master/LICENSE.txt
