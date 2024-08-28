from .base import *

import dj_database_url

# Database

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

ALLOWED_HOSTS = ['https://jakegodsall-portfolio-cf8c4e9d835b.herokuapp.com/']
