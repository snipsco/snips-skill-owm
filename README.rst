OpenWeatherMap skill for Snips
==============================

.. image:: https://travis-ci.org/snipsco/snips-skill-weather-owm.svg
   :target: https://travis-ci.org/snipsco/snips-skill-weather-owm
   :alt: Build Status

.. image:: https://img.shields.io/pypi/v/snipsowm.svg
   :target: https://pypi.python.org/pypi/snipsowm
   :alt: PyPI

Installation
------------

The skill is on PyPI, so you can just install it with `pip`_:

.. code-block:: console

    $ pip install snipsowm

Running
-------

To try out the skill, you can run the test server, providing your OpenWeatherMap API key (you can obtain one from the `OpenWeatherMap website`_) as well as the default location for weather forecasts:

.. code-block:: console

    $ python server.py --owm_api_key=YOUR_API_KEY --default_location=Paris,fr

Copyright
---------

This skill is open source, provided by `Snips`_. See `LICENSE.txt`_ for more
information.

.. _`pip`: http://www.pip-installer.org/
.. _`Snips`: https://www.snips.ai
.. _`OpenWeatherMap website`: https://openweathermap.org/api
.. _`LICENSE.txt`: https://github.com/snipsco/snips-skill-weather-owm/blob/master/LICENSE.txt
