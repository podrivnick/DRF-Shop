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

INSTALLED_APPS.append('drf_spectacular')  # noqa

SPECTACULAR_SETTINGS = {
   'TITLE': 'Shop',  # noqa
   'DESCRIPTION': 'Your API description',
   'VERSION': '1.0.0',
}

REST_FRAMEWORK['DEFAULT_SCHEMA_CLASS'] = 'drf_spectacular.openapi.AutoSchema'  # noqa
