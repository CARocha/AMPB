from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('noticias/', lista_noticias, name='lista-noticias'),
    path('noticias/por-pais/<slug>', filtro_noticias, name='filtro-noticias'),
    path('noticias/<slug>', detalle_noticia, name='detalle-noticia'),
    path('noticias/busqueda/', search_actualidad, name='search-actualidad'),
    path('galerias/', lista_galerias, name='lista-galerias'),
    path('galerias/por-pais/<slug>', filtro_galerias, name='filtro-galerias'),
    path('galerias/<slug>', detalle_galeria, name='detalle-galeria'),
    path('eventos/', lista_eventos, name='lista-eventos'),
    path('eventos/por-pais/<slug>', filtro_eventos, name='filtro-eventos'),
    path('eventos/<slug>', detalle_evento, name='detalle-evento'),
    path('eventos/busqueda/', search_evento, name='search-evento'),
    path('biblioteca/', lista_biblioteca, name='lista-biblioteca'),
    path('biblioteca/busqueda/', search_biblioteca, name='search-biblioteca'),
    path('quienes-somos/', quienes_somos, name='quienes-somos'),
    # path('biblioteca/por-pais/<slug>', filtro_biblioteca, name='filtro-biblioteca'),

    path('contactenos/', TemplateView.as_view(template_name="contactenos/contactenos.html")),
]
