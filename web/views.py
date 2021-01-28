from django.shortcuts import render
from .models import *
import datetime
from configuracion.models import *
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory
from haystack.forms import ModelSearchForm
from .forms import *
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.
def index(request,template='index.html'):
	banner = Banner.objects.order_by('-id')[:3]
	actualidad = Actualidad.objects.order_by('-id')[:6]
	hoy = datetime.date.today()
	eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	liderazgos = Liderazgo.objects.order_by('-id')[:4]
	galerias = Galeria.objects.order_by('-id')[:6]
	escuelas = Escuela.objects.all()
	return render(request, template, locals())

def lista_noticias(request,template='noticias/lista.html'):
	objects_list = Actualidad.objects.order_by('-fecha')
	paises = Actualidad.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	form = BuscadorForm
	return render(request, template, locals())

def filtro_noticias(request,slug=None,template='noticias/lista.html'):
	objects_list = Actualidad.objects.filter(escuela__pais__slug = slug).order_by('-fecha')
	paises = Actualidad.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	return render(request, template, locals())

def detalle_noticia(request,slug=None,template='noticias/detalle.html'):
	object = Actualidad.objects.get(slug = slug)
	relacionados = Actualidad.objects.filter(escuela = object.escuela).exclude(id = object.id)[:3]
	return render(request, template, locals())

def lista_galerias(request,template='galerias/lista.html'):
	objects_list = Galeria.objects.order_by('-id')
	paises = Galeria.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	return render(request, template, locals())

def filtro_galerias(request,slug=None,template='galerias/lista.html'):
	objects_list = Galeria.objects.filter(escuela__pais__slug = slug).order_by('-id')
	paises = Galeria.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	return render(request, template, locals())

def detalle_galeria(request,slug=None,template='galerias/detalle.html'):
	object = Galeria.objects.get(slug = slug)
	return render(request, template, locals())

def lista_eventos(request,template='eventos/lista.html'):
	objects_list = Evento.objects.order_by('-inicio')
	paises = Evento.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	form = BuscadorForm
	return render(request, template, locals())

def filtro_eventos(request,slug=None,template='eventos/lista.html'):
	objects_list = Evento.objects.filter(escuela__pais__slug = slug).order_by('-inicio')
	paises = Evento.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	return render(request, template, locals())

def detalle_evento(request,slug=None,template='eventos/detalle.html'):
	object = Evento.objects.get(slug = slug)
	return render(request, template, locals())

def lista_biblioteca(request,template='biblioteca/lista.html'):
	objects_list = Biblioteca.objects.order_by('-fecha')
	form = BuscadorForm
	return render(request, template, locals())

# def filtro_biblioteca(request,slug=None,template='biblioteca/lista.html'):
# 	objects_list = Biblioteca.objects.filter(escuela__pais__slug = slug).order_by('-id')
# 	paises = Biblioteca.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
# 	return render(request, template, locals())

def quienes_somos(request,template='quienes_somos.html'):
	object_list = QuienesSomos.objects.order_by('orden')
	return render(request, template, locals())


def contactenos(request,template='contactenos/contactenos.html'):
	if request.method == 'POST':
		form = ContactoForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			correo = form.cleaned_data['correo']
			telefono = form.cleaned_data['telefono']
			asunto = form.cleaned_data['asunto']
			mensaje = form.cleaned_data['mensaje']

			try:
				subject, from_email = asunto, 'mail@gmail.com'
				text_content =  render_to_string('contactenos/correo.txt', {'nombre': nombre, 'correo':correo, 'telefono':telefono, 'asunto':asunto, 'mensaje':mensaje})

				html_content = render_to_string('contactenos/correo.txt', {'nombre': nombre, 'correo':correo, 'telefono':telefono, 'asunto':asunto, 'mensaje':mensaje})

				msg = EmailMultiAlternatives(subject, text_content, from_email, ['comunicacion@escuelamesoamericana.org',])
				msg.attach_alternative(html_content, "text/html")
				msg.send()

				enviado = True
				messages.success(request, 'Success!')
				return HttpResponseRedirect(request.path)
			except:
				pass
	else:
		form = ContactoForm()

	return render(request, template, locals())

######## buscadores #############
def search_actualidad(request):
	sqs = SearchQuerySet().models(Actualidad).order_by('-id')
	view = search_view_factory(
		view_class=SearchView,
		template='search/search_actualidad.html',
		searchqueryset=sqs,
		form_class=ModelSearchForm
		)
	return view(request)

def search_evento(request):
	sqs = SearchQuerySet().models(Evento).order_by('-id')
	view = search_view_factory(
		view_class=SearchView,
		template='search/search_evento.html',
		searchqueryset=sqs,
		form_class=ModelSearchForm
		)
	return view(request)

def search_biblioteca(request):
	sqs = SearchQuerySet().models(Biblioteca).order_by('-id')
	view = search_view_factory(
		view_class=SearchView,
		template='search/search_biblioteca.html',
		searchqueryset=sqs,
		form_class=ModelSearchForm
		)
	return view(request)
