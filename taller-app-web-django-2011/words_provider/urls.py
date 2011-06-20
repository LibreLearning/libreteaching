from django.conf.urls.defaults import *
import django.views.static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^apps/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'apps'}),

    (r'^(.*)$', 'words_provider.words.views.gimmeword'),

)
