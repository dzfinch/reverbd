"""Production settings."""
import os

from .base import *  # noqa: F403
from .base import env_bool, env_list

DEBUG = False
ALLOWED_HOSTS = env_list("ALLOWED_HOSTS", ["localhost", "127.0.0.1"])

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = int(os.environ.get("SECURE_HSTS_SECONDS", "0"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = env_bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", False)
SECURE_HSTS_PRELOAD = env_bool("SECURE_HSTS_PRELOAD", False)

CSRF_TRUSTED_ORIGINS = env_list("CSRF_TRUSTED_ORIGINS")
