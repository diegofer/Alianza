from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home'),
    url(r'^quienes-somos/$', 'website.views.quienes_somos'),
    url(r'^update/?$', 'github.views.update'),

    #url(r'^estadistica/$', 'estadistica.views.shell'),
    #url(r'^estadistica/region/$', 'estadistica.views.region_vista'),
    # url(r'^Alianza/', include('Alianza.foo.urls')),

 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
