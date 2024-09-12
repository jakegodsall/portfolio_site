import os
import dj_database_url

from .base import *


# AWS S3

INSTALLED_APPS += ['storages']

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

AWS_S3_FILE_OVERWRITE = False  # Avoid overwriting files with the same name
AWS_DEFAULT_ACL = None  # Set default ACL to None to avoid public access by default
AWS_QUERYSTRING_AUTH = False  # Set this to False if you don't want query string auth for the files

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

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