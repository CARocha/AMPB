from django import template
from aprende.models import Contenidos
from itertools import chain

register = template.Library()

@register.filter(name='ids')
def ids(value):
    valores = Contenidos.objects.filter(modulo = value).values_list('id',flat=True)
    return list(set(chain(valores)))
