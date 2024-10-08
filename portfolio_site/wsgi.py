"""
WSGI config for portfolio_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

environment = os.getenv('DJANGO_ENV', 'development')
if environment == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings.development')

application = get_wsgi_application()
