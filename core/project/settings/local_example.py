from .main import *  # noqa


DEBUG = True
LOGIN_REDIRECT_URL = '/api/v1/products/'
ALLOWED_HOSTS = [
    "*",
]
ELASTIC_APM['DEBUG'] = DEBUG  # noqa

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]

# if DEBUG = True  noqa
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  noqa
# STATICFILES_DIRS = []  noqa
