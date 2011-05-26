
from django.conf.urls.defaults import *
from django.contrib import admin

import survey.views

import os

admin.autodiscover()

urlpatterns = patterns('',
    (r"^$", 'survey.views.survey'),
    (r"^survey/?", 'survey.views.survey'),
    (r"^surveyjs/?$", 'survey.views.surveyjs'),
    (r"^thanks/?$", 'survey.views.thanks'),
    (r'^admin/?', include(admin.site.urls)),

    # Example:
    # (r'^Superlatives/', include('Superlatives.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.static', 
  (r'^static/(?P<path>.*)$', 'serve', {
    'document_root': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static') }),
)

