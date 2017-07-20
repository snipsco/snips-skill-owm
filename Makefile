install:
	sudo apt-get install git python-pip
	sudo easy_install --upgrade pip
	sudo python setup.py install
	pip install pycodestyle
	pip install autopep8

format:
	sudo autopep8 --in-place --recursive .

check-codestyle:
	pycodestyle server.py
	pycodestyle snips_skill_weather_owm/weather.py

tests:
	python setup.py test