from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.home'),
    url(r'^quienes-somos/$', 'website.views.quienes_somos'),
    url(r'^noticia/(?P<id_noticia>\d+)$', 'website.views.detalle_noticia'),
    url(r'^peticiones/$', 'website.views.peticiones'),
    url(r'^update/?$', 'github.views.update'),

    #url(r'^estadistica/$', 'estadistica.views.shell'),
    #url(r'^estadistica/region/$', 'estadistica.views.region_vista'),
    # url(r'^Alianza/', include('Alianza.foo.urls')),

 	url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
