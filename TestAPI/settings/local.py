# settings/local.py
# Development environment settings
from .base import *
from os import environ

SECRET_KEY = get_env_variable('SECRET_KEY')
DEBUG = get_env_variable('DEBUG')
