from django.shortcuts import render
from .models import *
from web.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse
import json as simplejson
from .forms import *
import collections

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
	rubros = HomologacionFondos.objects.values_list('rubro','rubro__nombre','rubro__descripcion').distinct('rubro')
	total_presupuesto = HomologacionFondos.objects.aggregate(total = Sum('presupuesto__presupuesto'))['total']
	rubro_dict = {}
	presupuesto_dict = {}
	for x in rubros:
		ejecucion = Ejecucion.objects.filter(anioejecucion__presupuesto__homologacion_fondos__rubro = x[0]).aggregate(ejecucion = Sum('ejecucion'))['ejecucion']
		rubro_dict[x[1],x[2]] = ejecucion

		#presupuesto vs ejecucion
		total = Presupuesto.objects.filter(homologacion_fondos__rubro = x[0]).aggregate(total = Sum('presupuesto'))['total']
		ejecucion_total = Ejecucion.objects.filter(anioejecucion__presupuesto__homologacion_fondos__rubro = x[0]).aggregate(total = Sum('ejecucion'))['total']
		presupuesto_dict[x[1]] = total,ejecucion_total
	
	#fuentes de financiamiento
	fuente = HomologacionFondos.objects.values_list('presupuesto__fuente','presupuesto__fuente__nombre').distinct('presupuesto__fuente')
	fuente_dict = {}
	# for x in fuente:

	#Gráficos de barra de ejecución:
	list_ejecucion = []
	if request.method == 'POST':
		form = RubroForm(request.POST)
		if form.is_valid():
			rubro = form.cleaned_data['rubro']
			anio = form.cleaned_data['anio']

			for mes in MESES_CHOICES:
				ejecucion_mensual = Ejecucion.objects.filter(anioejecucion__presupuesto__homologacion_fondos__rubro__slug = rubro,
																anioejecucion__anio = anio, mes = mes[0]).values_list('ejecucion',flat=True)
				if ejecucion_mensual:
					list_ejecucion.append(ejecucion_mensual[0])
				else:
					list_ejecucion.append(0)
	else:
		form = RubroForm
	
	#graf fuente finan
	fuente_dict = {}
	fuente = FuenteFinanciamiento.objects.distinct('nombre')
	for x in fuente:
		presup_fuente = Presupuesto.objects.filter(fuente = x).aggregate(total = Sum('presupuesto'))['total']
		ejecucion_fuente = Ejecucion.objects.filter(anioejecucion__presupuesto__fuente = x).aggregate(total = Sum('ejecucion'))['total']
		fuente_dict[x] = presup_fuente,ejecucion_fuente
	
	#link divulgación
	divulgacion = Producto.objects.filter(rubro__nombre = 'Divulgación')

	tabla = HomologacionFondos.objects.all()
	list = collections.OrderedDict()
	for	obj in tabla:
		pre_list = collections.OrderedDict()
		list[obj.rubro] = pre_list
		for	pre in obj.presupuesto_set.all():
			anio_dict = collections.OrderedDict()
			pre_list[pre.presupuesto,pre.fuente.nombre,pre.saldo] = anio_dict	
			for	anio in pre.anioejecucion_set.all():
				anio_eje= collections.OrderedDict()
				anio_dict[anio.anio] = anio_eje
				for eje in anio.ejecucion_set.all():
					anio_eje[eje.mes] = eje.ejecucion
				

	return render(request, template, locals())