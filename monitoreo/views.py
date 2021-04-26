from django.shortcuts import render
from .models import *
from web.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
import json as simplejson
from .forms import *

# Create your views here.
def nucleos(request,template='nuestro-trabajo/nucleos.html'):
	escuelas = Escuela.objects.all()
	#graf jovenes
	mujeres = Escuela.objects.aggregate(total = Sum('mujeres'))['total']
	hombres = Escuela.objects.aggregate(total = Sum('hombres'))['total']
	otros = Escuela.objects.aggregate(total = Sum('otros'))['total']

	#conteos
	territorios = Escuela.objects.distinct('municipio').count()
	lideres = Participantes.objects.filter(cargo__nombre = 'Líder o directivo/a').count()
	formadores = Formadores.objects.count()
	emprendimientos = Emprendimientos.objects.count()

	return render(request, template, locals()) 

def detalle_nucleo(request,slug,template='nuestro-trabajo/detalle_nucleo.html'):
	object = Escuela.objects.get(slug=slug)
	emprendimientos = Emprendimientos.objects.filter(escuela = object)
	return render(request, template, locals()) 

@login_required
def formadores(request,template='nuestro-trabajo/formadores.html'):
	object = Formadores.objects.order_by('nombre')
	return render(request, template, locals())

@login_required
def participantes(request,template='nuestro-trabajo/participantes.html'):
	object = Participantes.objects.order_by('nombre')
	return render(request, template, locals())

def finanzas(request,template='nuestro-trabajo/finanzas.html'):
	#ejecucion x rubro
	rubros = HomologacionFondos.objects.values_list('rubro','rubro__nombre').distinct('rubro')
	total_presupuesto = HomologacionFondos.objects.aggregate(total = Sum('presupuesto__presupuesto'))['total']
	rubro_dict = {}
	for x in rubros:
		ejecucion = Ejecucion.objects.filter(anioejecucion__homologacion_fondos__rubro = x[0]).aggregate(ejecucion = Sum('ejecucion'))['ejecucion']
		rubro_dict[x[1]] = ejecucion
	
	#fuentes de financiamiento
	fuente = HomologacionFondos.objects.values_list('presupuesto__fuente','presupuesto__fuente__nombre').distinct('presupuesto__fuente')
	fuente_dict = {}
	# for x in fuente:

	#form = RubroForm
	return render(request, template, locals())

def ajax_rubro(request):
	slug = request.GET.get('slug', '')
	lista = []
	fondos = HomologacionFondos.objects.filter(rubro__slug = slug)
	presupuesto = fondos.aggregate(total = Sum('presupuesto__presupuesto'))['total']

	return HttpResponse(simplejson.dumps(list(fondos)), content_type = 'application/json')