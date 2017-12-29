# settings/local.py
# Development environment settings
from .base import *
from os import environ

SECRET_KEY = environ.get('SECRET_KEY')
DEBUG = environ.get('DEBUG')
