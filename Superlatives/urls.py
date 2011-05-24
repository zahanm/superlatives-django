from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r"/", survey.views.show_survey),
    (r"/surveyjs", survey.views.surveyjs),
    
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
    'document_root': os.path.join(os.path.dirname(os.path.absname(__file__)), 'static') }),
)

