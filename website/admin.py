from django.contrib import admin
from django.forms.widgets import TextInput

from website.models import Noticia, Youtube, Iglesia

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField


class IglesiaModelAdmin(admin.ModelAdmin):
	formfield_overrides = {
	    AddressField: {'widget': GoogleMapsAddressWidget},
	    GeoLocationField: {'widget': TextInput(attrs={'readonly': 'readonly'})},
	}


admin.site.register(Noticia)
admin.site.register(Youtube)
admin.site.register(Iglesia, IglesiaModelAdmin)