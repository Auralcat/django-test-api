# settings/local.py
# Development environment settings
from .base import *

DEBUG = get_env_variable('DEBUG')

CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = None
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_FRAME_DENY = False
