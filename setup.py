from setuptools import setup

setup(
    name='snips_skill_weather_owm',
    version='0.1.0',
    description='OpenWeatherMap weather skill for Snips',
    author=['Michael Fester'],
    author_email=['michael.fester@snips.ai'],
    url='https://www.snips.ai',
    download_url='',
    license='MIT',
    install_requires=['paho-mqtt', 'requests==2.6.0', 'pyyaml'],
    test_suite="tests",
    packages=[
        'snips_skill_weather_owm'
    ]
)
