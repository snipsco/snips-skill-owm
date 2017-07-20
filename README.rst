OpenWeatherMap skill for Snips
==============

.. image:: https://travis-ci.org/snipsco/snips-skill-weather-owm.svg
   :target: https://travis-ci.org/snipsco/snips-skill-weather-owm
   :alt: Build Status

Installation
------------

The skill is on PyPI, so you can just install it with `pip`_:

.. code-block:: console

    $ pip install snipsowm

Running
-------

Start the skill server by running the following command, providing your OpenWeatherMap API key ((generate one here)[]) as well as the default location for weather forecasts:

.. code-block:: console

    $ python server.py --owm_api_key=YOUR_API_KEY --default_location=Paris,fr

Copyright
---------

This skill is open source, provided by `Snips`_. See 


.. _`pip`: http://www.pip-installer.org/
.. _`Snips`: https://www.snips.ai
