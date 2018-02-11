""" Development related settings."""
import sys

from .base import *

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ALLOWED_HOSTS = []

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
 'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': os.environ.get('DB_NAME'),
      'USER': os.environ.get('DB_USER'),
      'PASSWORD': os.environ.get('DB_PASSWORD'),
      'PORT': os.environ.get('DB_PORT'),
      'TEST': {
        'CHARSET': None,
        'COLLATION': None,
        'NAME': os.path.join(os.path.dirname(__file__), 'test.db'),
        'MIRROR': None
      }
  }
 }

