import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Org Zero - Prompt",
    version = "0.0.1",
    author = "Brian Bokor",
    author_email = "brian.bokor@gmail.com",
    description = ("Demostration of mad SWE skills."),
    packages=[
        'models',
        'parser',
        'prompt',
        'report',
        'tests/models',
        'tests/parser',
        'tests/report',
    ],
)
