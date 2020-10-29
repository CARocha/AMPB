from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'cursos', CursosViewSet)
router.register(r'contenidos', ContenidoViewSet)
router.register(r'modulos', ModuloViewSet)

urlpatterns = [
	path('api/',include(router.urls)),
	path('api/modulos/filtro/<id>', ModulosFiltrado.as_view()),
	path('api/contenidos/filtro/<id>', ContenidosFiltrado.as_view()),
	path('', lista_cursos, name='lista-cursos'),
	path('<slug>/', detalle_curso, name='detalle-curso'),
	path('<slug>/<id>/', detalle_contenido, name='detalle-contenido')
]