from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cursos', views.CursosViewSet)
router.register(r'contenidos', views.ContenidoViewSet)
router.register(r'modulos', views.ModuloViewSet)

urlpatterns = [
	path('api/',include(router.urls)),
]