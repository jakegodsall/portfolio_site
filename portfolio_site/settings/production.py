import os
import dj_database_url

from .base import *

# Security

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include subdomains
SECURE_HSTS_PRELOAD = True  # Enable HSTS preload list
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# AWS S3

INSTALLED_APPS += ['storages']

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

AWS_S3_FILE_OVERWRITE = True
AWS_DEFAULT_ACL = None  # Set default ACL to None to avoid public access by default
AWS_QUERYSTRING_AUTH = False  # Set this to False if you don't want query string auth for the files

# For static files
STATICFILES_DIRS = [
    BASE_DIR / "portfolio" / "staticfiles",
]
AWS_STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
STATICFILES_STORAGE = 'portfolio_site.storages.StaticStorage'

# For media files
AWS_MEDIA_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'portfolio_site.storages.MediaStorage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/'

# Database

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

# Anki App
ANKI_USER = os.getenv('ANKI_USER', 'User 1')
ANKI_COLLECTION_PATH = os.getenv('ANKI_COLLECTION_PATH')
ANKI_COLLECTION_FILE_NAME = os.getenv('ANKI_COLLECTION_FILE_NAME')
ANKI_DECKS = os.getenv('ANKI_DECKS', '*').split(',')

