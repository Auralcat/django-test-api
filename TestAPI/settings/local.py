# settings/local.py
# Development environment settings
from .base import *

DEBUG = get_env_variable('DEBUG')
