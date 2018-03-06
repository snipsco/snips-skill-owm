from setuptools import setup, find_packages

setup(
    name='snipsowm',
    version='0.2.1',
    description='OpenWeatherMap weather skill for Snips',
    author='Michael Fester',
    author_email='michael.fester@gmail.com',
    url='https://github.com/snipsco/snips-skill-owm',
    download_url='',
    license='MIT',
    install_requires=[
        'requests==2.6.0',
        'enum34==1.1.6',
        'python-Levenshtein'
    ],
    test_suite="tests",
    keywords=['snips'],
    package_data={'snipsowm': ['Snipsspec']},
    packages=find_packages()
)
