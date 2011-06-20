from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^login', 'django.contrib.auth.views.login'),
    (r'^logout', 'django.contrib.auth.views.logout'),

    (r'^(.*)$', 'cms_users.content.views.show_content',),
)
