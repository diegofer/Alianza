from django import forms
from django.db import models
from website.widgets import LocationWidget

class LocationFormField(forms.CharField):
    
    def clean(self, value):
        
        if value is u'' or value is None:
            return None
        
        if isinstance(value, unicode):
            a, b = value.split(',')
        else:
            a, b = value
        
        lat, lng = float(a), float(b)
        return "%f,%f" % (lat, lng)

class LocationField(models.CharField):
    
    def formfield(self, **kwargs):
        defaults = {
            'form_class': LocationFormField
        }
        defaults.update(kwargs)
        defaults['widget'] = LocationWidget
        
        return super(LocationField, self).formfield(**defaults)