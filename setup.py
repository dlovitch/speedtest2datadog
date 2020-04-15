from setuptools import setup, find_packages

requires = [
    "click",
    "datadog",
    "pylint",
    "speedtest-cli"
    ]

setup(
    name='speedtest2datadog',
    version='0.0.1',
    description='send speedtest stats to datadog',
    url='https://github.com/dlovitch/speedtest2datadog',
    python_requires='>3.8.1',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            "st2dd=speedtest2datadog.cli:cli",
        ],
    },
)
