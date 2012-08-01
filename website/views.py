#encoding:utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from website.models import  Noticia, Youtube
from website.forms import PeticionesForm
from django.core.mail import EmailMessage

def home(request):
	noticias = Noticia.objects.all().order_by('-fecha').filter(activado=True)[0:5]
	try:
		video = Youtube.objects.all().order_by('-fecha').filter(activado=True)[0]
	except Youtube.DoesNotExist:
		video = None
	
	return render_to_response('website/home.html',{'noticias':noticias, 'youtube':video}, context_instance=RequestContext(request))

def primera_vez(request):
	titulo = '¿Primera vez<br/> <span>en este sitio?</span>'
	return render_to_response('website/primera-vez.html', {'titulo':titulo}, context_instance=RequestContext(request))

def nosotros(request):
	imag = 'reloj1.jpg'
	titulo = 'CUANDO TODO EMPEZO'
	return render_to_response('website/nosotros.html',{'imag':imag, 'titulo':titulo}, context_instance=RequestContext(request))

def detalle_noticia(request, noticia_slug):
	dato = get_object_or_404(Noticia, slug=noticia_slug)
	return render_to_response('website/noticia.html', {'noticia':dato}, context_instance=RequestContext(request))

def peticiones(request):
 	form = PeticionesForm(request.POST or None)
 	if form.is_valid():
 		titulo = 'Petición de oración desde web Alianza'
 		content = form.cleaned_data['peticion'] + "\n"
 		content += 'responder a: ' + form.cleaned_data['correo'] + "\n"
 		content += 'de: ' + form.cleaned_data['nombre'] + "\n"
 		content += 'vive en: ' + form.cleaned_data['ciudad'] 
 		correo = EmailMessage(titulo, content, to=['diegofernando83@gmail.com'])
 		correo.send()
 		return HttpResponseRedirect('/peticiones')
 	return render_to_response('website/peticiones.html', {'form':form}, context_instance=RequestContext(request))

