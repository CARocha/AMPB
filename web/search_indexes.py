from haystack import indexes
from .models import *

class NoticiaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    resumen = indexes.CharField(model_attr='contenido', null=True)

    def get_model(self):
        return Actualidad

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-id')
