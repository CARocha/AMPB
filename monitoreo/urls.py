from django.urls import path
from .views import *

urlpatterns = [
    path('formadores/', formadores, name='formadores'),
]