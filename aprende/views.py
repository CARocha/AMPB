from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer

class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenidos.objects.all()
    serializer_class = ContenidoSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulos.objects.all()
    serializer_class = ModulosSerializer

def lista_cursos(request,template='aprende/lista.html'):
    objects_list = Cursos.objects.filter(activo = True).order_by('-id')
    return render(request, template, locals())

def detalle_curso(request,slug=None,template='aprende/detalle.html'):
    object = Cursos.objects.get(slug = slug)
    return render(request, template, locals())