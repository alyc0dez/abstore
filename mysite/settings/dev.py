from .common import *

DEBUG = True

SECRET_KEY = 'm9@7b61n13df($l!%bnia1@9yopgfittos+d!(lr#d9pdnwa!n'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ab_store',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'bain467gain'
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '2525'