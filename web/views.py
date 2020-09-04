from django.shortcuts import render
from .models import *

# Create your views here.
def index(request,template='index.html'):
	banner = Banner.objects.order_by('-id')[:3]
	actualidad = Actualidad.objects.order_by('-id')[:6]
	return render(request, template, locals())
