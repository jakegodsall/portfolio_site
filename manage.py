#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    # Determine the environment
    environment = os.getenv('DJANGO_ENV', 'development')
    # Set the settings module

    if environment == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings.production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings.development')
    print(f"DJANGO_SETTINGS_MODULE is set to: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
