from django.shortcuts import render
from rest_framework import viewsets,generics
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

class ContenidosFiltrado(generics.ListAPIView):
    serializer_class = ContenidoSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Contenidos.objects.filter(modulo__curso = id)

class ModulosFiltrado(generics.ListAPIView):
    serializer_class = ModulosSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Modulos.objects.filter(curso = id)

def lista_cursos(request,template='aprende/lista.html'):
    objects_list = Cursos.objects.filter(activo = True).order_by('-id')
    return render(request, template, locals())

def detalle_curso(request,slug=None,template='aprende/detalle.html'):
    object = Cursos.objects.get(slug = slug)
    return render(request, template, locals())