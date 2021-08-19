import datetime
from haystack import indexes
from .models import *

class ActualidadIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    resumen = indexes.CharField(model_attr='contenido', null=True)
    fecha = indexes.DateTimeField(model_attr='fecha')

    def get_model(self):
        return Actualidad

    def index_queryset(self, using=None):
        #return self.get_model().objects.order_by('-id')
        return self.get_model().objects.filter(fecha__lte=datetime.datetime.now())

class EventoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    descripcion = indexes.CharField(model_attr='descripcion', null=True)
    fin = indexes.DateTimeField(model_attr='fin')

    def get_model(self):
        return Evento

    def index_queryset(self, using=None):
        #return self.get_model().objects.order_by('-id')
        return self.get_model().objects.filter(fin__lte=datetime.datetime.now())

class BibliotecaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    nombre = indexes.NgramField(model_attr='nombre')
    descripcion = indexes.NgramField(model_attr='descripcion', null=True)

    def get_model(self):
        return Biblioteca

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-id')

class ExperienciaLiderazgoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)
    titulo = indexes.NgramField(model_attr='titulo')
    resumen = indexes.NgramField(model_attr='contenido', null=True)

    def get_model(self):
        return ExperienciaLiderazgo

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-id')
