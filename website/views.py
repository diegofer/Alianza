#encoding:utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from website.models import  noticia
from website.forms import PeticionesForm
from django.core.mail import EmailMessage

def home(request):
	noticias = noticia.objects.all()
	return render_to_response('website/home.html',{'noticias':noticias}, context_instance=RequestContext(request))

def quienes_somos(request):
	return render_to_response('website/quienes-somos.html', context_instance=RequestContext(request))

def nosotros(request):
	return render_to_response('website/nosotros.html', context_instance=RequestContext(request))

def detalle_noticia(request, id_noticia):
	dato = get_object_or_404(noticia, pk=id_noticia)
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

