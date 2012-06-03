
import os
import sys

sys.path.insert(0, '/var/django/superlatives/superlatives/') # Put path to project here.

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
