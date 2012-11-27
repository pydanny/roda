from base import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Audrey Roy', 'audreyr@cartwheelweb.com'),
    ('Daniel Greenfeld', 'pydanny@cartwheelweb.com'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL',
        'roda <info@roda.com>')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)
SERVER_EMAIL = 'info@roda.com'
EMAIL_USE_TLS = True


from postgresify import postgresify

DATABASES = postgresify()

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

########## STORAGE CONFIGURATION
#INSTALLED_APPS += ('storages', 'raven.contrib.django', )

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2020 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

# Boto requires subdomain formatting.
from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

# Amazon S3 configuration.
if 'AWS_ACCESS_KEY_ID' in os.environ:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
else:
    raise Exception("Missing AWS_ACCESS_KEY_ID")

if 'AWS_SECRET_ACCESS_KEY' in os.environ:
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
else:
    raise Exception("Missing AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = 'roda'

STATIC_URL = 'https://s3.amazonaws.com/roda/'
MEDIA_URL = STATIC_URL
########## END STORAGE CONFIGURATION

DJANGO_WYSIWYG_MEDIA_URL = os.path.join(STATIC_URL, 'ckeditor')
