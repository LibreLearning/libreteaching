from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('myproject.myfirstapp.views',
                       (r'^$', 'say_main',),
                       (r'^hello', 'say_hello',),
                       (r'^bye/(.*)', 'say_bye_to',),
                       (r'^number/(?P<number>[\d]+)', 'say_number',),
    # Example:
    # (r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
