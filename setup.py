from setuptools import setup

setup(
    name='snips_skill_weather',
    version='0.1.0',
    description='',
    author=['Michael Fester'],
    author_email=['michael.fester@snips.ai'],
    url='',
    download_url='',
    license='MIT',
    install_requires=['paho-mqtt','requests==2.6.0'.'pyyaml'],
    tests_require=[],
    packages=[
        'snips_skill_weather'
    ]
)
