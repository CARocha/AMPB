from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def formadores(request,template='nuestro-trabajo/formadores.html'):
    object = Formadores.objects.order_by('nombre')
    return render(request, template, locals())
