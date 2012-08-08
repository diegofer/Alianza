from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'website.views.home'),
    url(r'^nosotros/$', 'website.views.nosotros'),
    url(r'^noticias/(?P<noticia_slug>.+?)/?$', 'website.views.detalle_noticia'),
    url(r'^primera-vez/$', 'website.views.primera_vez'), 
    url(r'^peticiones/$', 'website.views.peticiones'),
    url(r'^sedes/$', 'website.views.sedes'),
    url(r'^update/?$', 'github.views.update'),

    #url(r'^estadistica/$', 'estadistica.views.shell'),
    #url(r'^estadistica/region/$', 'estadistica.views.region_vista'),
    # url(r'^Alianza/', include('Alianza.foo.urls')),

 	url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
