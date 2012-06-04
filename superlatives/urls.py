
from django.conf.urls.defaults import *
from django.contrib import admin

import survey.views

import os

admin.autodiscover()
admin.site.login_template = 'webauth/admin_redirect.html'

urlpatterns = patterns('',
    (r"^$", 'survey.views.survey'),
    (r"^survey/?$", 'survey.views.survey'),
    (r"^surveyjs/?$", 'survey.views.surveyjs'),
    (r"^results/?$", 'survey.views.results'),
    (r"^thanks/?$", 'survey.views.thanks'),
    (r'^admin/?', include(admin.site.urls)),
    (r'^webauth/', include('webauth.urls'))
)
