from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def index(request,template='index.html'):
	banner = Banner.objects.order_by('-id')[:3]
	actualidad = Actualidad.objects.order_by('-id')[:6]
	hoy = datetime.date.today()
	eventos = Evento.objects.filter(inicio__gte = hoy).order_by('inicio')[:1]
	liderazgos = Liderazgo.objects.order_by('-id')[:4]
	return render(request, template, locals())
