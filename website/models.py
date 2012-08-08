#encoding:utf-8
from django.db import models
from thumbs import ImageWithThumbsField
from django_google_maps.fields import AddressField, GeoLocationField

#from django.utils.translation import ugettext as _

class Noticia(models.Model):
	titulo    = models.CharField(max_length=150, unique=True)
	slug      = models.CharField(max_length=300, help_text='Ej. titulo-de-la-noticia')
	contenido = models.TextField(help_text='Redacte el contenido')
	imagen	  = ImageWithThumbsField(upload_to='noticias', sizes=((200,87),(500,218)), verbose_name='Imágen', help_text='Solo imágenes con formato JPG y tamano de 1024X445')
	fecha 	  = models.DateTimeField(auto_now=True)
	activado  = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.titulo
		
class Youtube(models.Model):
	titulo     = models.CharField(max_length=100, unique=True)
	embed_code = models.TextField(help_text='código que da el canal de youtube para insertar el video')
	fecha 	   = models.DateTimeField(auto_now=True)
	categoria  = models.CharField(max_length=100)
	activado   = models.BooleanField(default=False)

	def __unicode__(self):
		return self.titulo

class Iglesia(models.Model):
	alias       = models.CharField(max_length=100, help_text='Slogan de la iglesia o Barrio, sector o corregimiento')
	pastor      = models.CharField(max_length=100, blank=True, help_text='Pastor director principal')
	tel         = models.CharField(max_length=100, blank=True, help_text='Puede introducir varios números de contacto')
	direccion   = models.CharField(max_length=100, blank=True, help_text='ej. calle 7 # 11-46')
	codigo      = models.IntegerField(max_length=4)
	web         = models.CharField(max_length=200, blank=True, help_text='Página web propia o de facebook u otra similar')
	address     = AddressField(max_length=100)
	geolocation = GeoLocationField(blank=True)
	
	def __unicode__(self):
		return '%s sede %s' % (self.address, self.alias)
