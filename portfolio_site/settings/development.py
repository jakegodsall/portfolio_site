from .base import *

DEBUG = True

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data' / 'database.db'
    }
}

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,13.41.193.107').split(',')

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

