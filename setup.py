from setuptools import setup
from os import path


def open_file(fname):
    return open(path.join(path.dirname(__file__), fname))

setup(
    name='django-alexa',
    author='Kyle Rockman',
    author_email='kyle.rockman@mac.com',
    summary='Amazon Alexa Skills Kit integration for Django',
    url='https://github.com/rocktavious/django-alexa',
    description='* Documentation: https://github.com/rocktavious/django-alexa',
    license_file='LICENSE'
    install_requires=open(path.join(path.dirname(__file__), 'requirements.txt')).readlines(),
)
