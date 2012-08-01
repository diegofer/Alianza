#encoding:utf-8
from django.db import models
from thumbs import ImageWithThumbsField

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
