# Django settings for superlatives project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Brennan Saeta', 'saeta@stanford.edu'),
    ('Zahan Malkani', 'zahanm@stanford.edu')
)

MANAGERS = ADMINS

STAFF_SUNETIDS = frozenset(['zahanm', 'ssterman'])

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join( os.path.dirname(os.path.abspath(__file__)), 'db/cardsuperdb.sqlite3' )
  }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# media and static
# MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
# MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y8#(+4&$v_*u_m5cidi9q9ajcxx=9!*=%5dwi!m(ix0zo7u#z6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'webauth.middleware.WebauthMiddleware'
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
)

STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deployed')
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'webauth',
    'survey',
)

# Family feud specific settings
FEUD_DATE_TIME = '5:30pm, Saturday June 9'

# Webauth configuration
WEBAUTH_SHARED_SECRET = '1472744213804086233448376697319099995645' # just some random secret
WEBAUTH_URL = 'https://www.stanford.edu/~pcostell/cgi-bin/wa-authenticate.php'
LOGIN_URL = '/webauth/login'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
BASE_URL = 'http://superlatives.zahanm.com/'
