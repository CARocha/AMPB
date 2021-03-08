from django.shortcuts import render
from .models import *
from web.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

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
    return render(request, template, locals()) 

@login_required
def formadores(request,template='nuestro-trabajo/formadores.html'):
    object = Formadores.objects.order_by('nombre')
    return render(request, template, locals())

@login_required
def participantes(request,template='nuestro-trabajo/participantes.html'):
    object = Participantes.objects.order_by('nombre')
    return render(request, template, locals())
