from .defaults import *  # noqa: F401, F403

DEBUG = True

# Celery
# CELERY_BROKER_URL = 'amqp://%s:%s@rabbit:5672' % (os.environ.get('RABBITMQ_DEFAULT_USER'), os.environ.get(
#     'RABBITMQ_DEFAULT_PASS'))  # using rabbitmq
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
