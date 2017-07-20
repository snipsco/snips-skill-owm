from setuptools import setup

setup(
    name='snipsowm',
    version='0.1.1',
    description='OpenWeatherMap weather skill for Snips',
    author='Michael Fester',
    author_email='michael.fester@gmail.com',
    url='https://github.com/snipsco/snips-skill-weather-owm',
    download_url='',
    license='MIT',
    install_requires=['paho-mqtt', 'requests==2.6.0', 'pyyaml'],
    test_suite="tests",
    keywords = ['snips'],
    packages=[
        'snipsowm'
    ]
)
