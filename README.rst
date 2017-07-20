OpenWeatherMap skill for Snips
==============================

|Build Status| |PyPI| |MIT License|


Installation
------------

The skill is on `PyPI`_, so you can just install it with `pip`_:

.. code-block:: console

    $ pip install snipsowm

Running
-------

To try out the skill, you can run the test server, providing your OpenWeatherMap API key (you can obtain one from the `OpenWeatherMap website`_) as well as the default location for weather forecasts:

.. code-block:: console

    $ python server.py --owm_api_key=YOUR_API_KEY --default_location=Paris,fr

Copyright
---------

This skill is provided by `Snips`_ as Open Source software. See `LICENSE.txt`_ for more
information.

.. |Build Status| image:: https://travis-ci.org/snipsco/snips-skill-weather-owm.svg
   :target: https://travis-ci.org/snipsco/snips-skill-weather-owm
   :alt: Build Status
.. |PyPI| image:: https://img.shields.io/pypi/v/snipsowm.svg
   :target: https://pypi.python.org/pypi/snipsowm
   :alt: PyPI
.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/snipsco/snips-skill-weather-owm/master/LICENSE.txt
   :alt: MIT License

.. _`PyPI`: https://pypi.python.org/pypi/snipsowm
.. _`pip`: http://www.pip-installer.org
.. _`Snips`: https://www.snips.ai
.. _`OpenWeatherMap website`: https://openweathermap.org/api
.. _`LICENSE.txt`: https://github.com/snipsco/snips-skill-weather-owm/blob/master/LICENSE.txt
