from django import forms
from .models import *


def rubros_choice():
    rubro = []
    rubro.append(('','-----'))
    for x in HomologacionFondos.objects.values_list('rubro__slug','rubro__nombre').distinct('rubro'):
        rubro.append((x[0],x[1]))
    return list(sorted(set(rubro)))

class RubroForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(RubroForm, self).__init__(*args, **kwargs)
		self.fields['rubro'] = forms.ChoiceField(choices=rubros_choice(),required = True)