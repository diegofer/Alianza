#encoding:utf-8
from django.db import models

class noticia(models.Model):
	titulo    = models.CharField(max_length=100, unique=True)
	contenido = models.TextField(help_text='Redacte el contenido')
	imagen    = models.ImageField(upload_to='noticias', verbose_name='Imágen')
	fecha 	  = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.titulo
		
