# If local.py is present, any settings in it will override those in base.py and dev.py.
# Use this for any settings that are specific to this one installation, such as developer API keys.
# local.py should not be checked in to version control.

from .dev import *

# Removes the debug toolbar tuple additions made in dev.py. Useful if debug toolbar is slowing down a dev site
# INSTALLED_APPS = INSTALLED_APPS[:-1]
# MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES[:-1]

EMBEDLY_KEY = 'get-one-from-http://embed.ly/'

STRIPE_SECRET_KEY = ""
STRIPE_PUBLISHABLE_KEY = ""


SECRET_KEY=os.getenv('DJANGO_SECRET_KEY','')

DATABASES = {
    'default':
        {'HOST': 'localhost', 'USER': os.getenv('DATABASE_USER',''), 'PASSWORD': os.getenv('DATABASE_PASSWORD',''), 'ENGINE': 'django.db.backends.postgresql_psycopg2', 'PORT': '', 'NAME': os.getenv('DATABASE_NAME','')}
}

