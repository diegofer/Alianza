#encoding:utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from django.core.mail import EmailMessage
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils import simplejson


from website.models import  Noticia, Youtube, Iglesia
from website.forms import PeticionesForm


##################  INICIO ##########################

def home(request):
	noticias = Noticia.objects.all().order_by('-fecha').filter(activado=True)[1:5]
	try:
		video = Youtube.objects.all().filter(activado=True).order_by('-fecha')[0]
	except Youtube.DoesNotExist:
		video = None
	return render_to_response('website/home.html',{'noticias':noticias, 'youtube':video}, context_instance=RequestContext(request))

def peticiones(request):
	titulo = 'Peticiones de<br/> <span>Oración</span>'
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
 	return render_to_response('website/peticiones.html', {'form':form, 'titulo':titulo}, context_instance=RequestContext(request))

def primera_vez(request):
	titulo = '¿Primera vez<br/> <span>en este sitio?</span>'
	return render_to_response('website/primera-vez.html', {'titulo':titulo}, context_instance=RequestContext(request))

@ensure_csrf_cookie
def sedes(request):
	titulo = 'La Alianza<br/> <span>en Colombia</span>'
	if request.is_ajax():
		q     = Iglesia.objects.all()
		sedes = serializers.serialize("json", q)
		return HttpResponse(sedes, mimetype='application/json') 
	return render_to_response('website/sedes.html', {'titulo':titulo}, context_instance=RequestContext(request))


##################  NOSOTROS ##########################

def nosotros(request):
	imag = 'reloj1.jpg'
	titulo = 'CUANDO TODO EMPEZO'
	return render_to_response('website/nosotros.html',{'imag':imag, 'titulo':titulo}, context_instance=RequestContext(request))

def vision(request):
	titulo = 'Nuestra<br/> <span>Visión</span>'
	return render_to_response('website/vision.html',{'titulo':titulo}, context_instance=RequestContext(request))

def creemos(request):
	titulo = 'Conoce más<br/> <span class="mediana">de la Alianza...</span>'
	return render_to_response('website/creemos.html',{'titulo':titulo}, context_instance=RequestContext(request))

def simbolos(request):
	titulo = 'Conoce más<br/> <span class="mediana">de la Alianza...</span>'
	return render_to_response('website/simbolos.html',{'titulo':titulo}, context_instance=RequestContext(request))

def fundaciones(request):
	titulo = 'Conoce más<br/> <span class="mediana">de la Alianza...</span>'
	return render_to_response('website/fundaciones.html',{'titulo':titulo}, context_instance=RequestContext(request))

def objetivos(request):
	titulo = 'Conoce más<br/> <span class="mediana">de la Alianza...</span>'
	return render_to_response('website/objetivos.html',{'titulo':titulo}, context_instance=RequestContext(request))

def objetivos(request):
	titulo = 'Conoce más<br/> <span class="mediana">de la Alianza...</span>'
	return render_to_response('website/objetivos.html',{'titulo':titulo}, context_instance=RequestContext(request))

def efi(request):
	titulo = 'Conoce más<br/> <span class="mediana">de la Alianza...</span>'
	return render_to_response('website/efi.html',{'titulo':titulo}, context_instance=RequestContext(request))

def logros(request):
	titulo = 'Conoce más<br/> <span class="mediana">de la Alianza...</span>'
	return render_to_response('website/logros.html',{'titulo':titulo}, context_instance=RequestContext(request))


##################  MISION ##########################

def mision(request):
	titulo = 'Nuestra<br/> <span>Misión</span>'
	return render_to_response('website/mision.html',{'titulo':titulo}, context_instance=RequestContext(request))

##################  MINISTERIOS ######################

def misiones(request):
	return render_to_response('website/misiones.html', context_instance=RequestContext(request))



##################  NOTICIAS ##########################

def detalle_noticia(request, noticia_slug):
	dato = get_object_or_404(Noticia, slug=noticia_slug)
	return render_to_response('website/noticia.html', {'noticia':dato}, context_instance=RequestContext(request))



