from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import *
from .models import *
from next_prev import next_in_order, prev_in_order

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

class ReflexionViewSet(viewsets.ModelViewSet):
    queryset = Reflexion.objects.all()
    serializer_class = ReflexionSerializer

def lista_cursos(request,template='aprende/lista.html'):
    objects_list = Cursos.objects.filter(activo = True).order_by('-id')
    reflexiones = Reflexion.objects.filter(activo = True).order_by('-fecha_creacion')[:3]
    return render(request, template, locals())

def detalle_curso(request,slug=None,template='aprende/detalle.html'):
    object = Cursos.objects.get(slug = slug)
    primer_contenido = Contenidos.objects.filter(modulo__curso = object).first()
    return render(request, template, locals())

def detalle_contenido(request,slug=None,id=None,template='aprende/detalle.html'):
    object = Cursos.objects.get(slug = slug)
    #contenidos
    contenido = Contenidos.objects.get(id = id)
    todos_contenidos = Contenidos.objects.filter(modulo__curso = object).order_by('modulo','id')
    siguiente = next_in_order(contenido, qs = todos_contenidos)
    anterior = prev_in_order(contenido, qs = todos_contenidos)

    #modulos
    modulo_actual = Modulos.objects.get(curso = object, contenidos = contenido)
    todos_modulos = Modulos.objects.filter(curso = object).order_by('curso','id')
    modulo_siguiente = next_in_order(modulo_actual, qs = todos_modulos)
    modulo_anterior = prev_in_order(modulo_actual, qs = todos_modulos)
    primer_modulo = Modulos.objects.filter(curso = object).first()
    ultimo = prev_in_order(primer_modulo, loop=True)

    ######
    last_path_id = int(request.path.split("/")[-2])


    return render(request, template, locals())
