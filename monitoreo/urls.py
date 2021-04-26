from django.urls import path
from .views import *

urlpatterns = [
    path('nucleos/', nucleos, name='nucleos'),
    path('nucleos/<slug>/', detalle_nucleo, name='detalle-nucleo'),
    path('participantes/', participantes, name='participantes'),
    path('formadores/', formadores, name='formadores'),
    path('finanzas/', finanzas, name='finanzas'),
    path('ajax/rubro/', ajax_rubro),
]