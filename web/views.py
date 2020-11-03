from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def index(request,template='index.html'):
	banner = Banner.objects.order_by('-id')[:3]
	actualidad = Actualidad.objects.order_by('-id')[:6]
	hoy = datetime.date.today()
	eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:3]
	liderazgos = Liderazgo.objects.order_by('-id')[:4]
	galerias = Galeria.objects.order_by('-id')[:6]
	return render(request, template, locals())

def lista_noticias(request,template='noticias/lista.html'):
	objects_list = Actualidad.objects.order_by('-id')
	paises = Actualidad.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	return render(request, template, locals())

def filtro_noticias(request,slug=None,template='noticias/lista.html'):
	objects_list = Actualidad.objects.filter(escuela__pais__slug = slug).order_by('-id')
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
	objects_list = Evento.objects.order_by('-id')
	paises = Evento.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	return render(request, template, locals())

def filtro_eventos(request,slug=None,template='eventos/lista.html'):
	objects_list = Evento.objects.filter(escuela__pais__slug = slug).order_by('-id')
	paises = Evento.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
	return render(request, template, locals())

def detalle_evento(request,slug=None,template='eventos/detalle.html'):
	object = Evento.objects.get(slug = slug)
	return render(request, template, locals())

def lista_biblioteca(request,template='biblioteca/lista.html'):
	objects_list = Biblioteca.objects.order_by('-id')
	return render(request, template, locals())

# def filtro_biblioteca(request,slug=None,template='biblioteca/lista.html'):
# 	objects_list = Biblioteca.objects.filter(escuela__pais__slug = slug).order_by('-id')
# 	paises = Biblioteca.objects.values_list('escuela__pais__slug','escuela__pais__nombre').distinct('escuela__pais')
# 	return render(request, template, locals())
