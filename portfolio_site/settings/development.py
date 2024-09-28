from .base import *

DEBUG = True

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
EMAIL_TIMEOUT = 10


CSRF_COOKIE_DOMAIN = 'None'

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']

ANKI_USER = os.getenv('ANKI_USER', 'User 1')
ANKI_COLLECTION_PATH = os.getenv('ANKI_COLLECTION_PATH')
ANKI_COLLECTION_FILE_NAME = os.getenv('ANKI_COLLECTION_FILE_NAME')
ANKI_DECKS = os.getenv('ANKI_DECKS', '*').split(',')

