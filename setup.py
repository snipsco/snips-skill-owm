from setuptools import setup

setup(
    name='snipsowm',
    version='0.1.3',
    description='OpenWeatherMap weather skill for Snips',
    author='Michael Fester',
    author_email='michael.fester@gmail.com',
    url='https://github.com/snipsco/snips-skill-owm',
    download_url='',
    license='MIT',
    install_requires=['requests==2.6.0'],
    test_suite="tests",
    keywords = ['snips'],
    packages=[
        'snipsowm'
    ]
)
