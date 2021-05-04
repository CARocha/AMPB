from django import forms
from .models import *


def rubros_choice():
	rubro = []
	rubro.append(('','-----'))
	for x in HomologacionFondos.objects.values_list('rubro__slug','rubro__nombre').distinct('rubro'):
		rubro.append((x[0],x[1]))
	return list(sorted(set(rubro)))

def anios_choice():
	anios = []
	# anios.append(('','-----'))
	for x in AnioEjecucion.objects.values_list('anio',flat=True).distinct('anio'):
		anios.append((x,x))
	return list(sorted(set(anios)))

class RubroForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(RubroForm, self).__init__(*args, **kwargs)
		self.fields['rubro'] = forms.ChoiceField(choices=rubros_choice(),required = True)
		self.fields['anio'] = forms.ChoiceField(choices=anios_choice(), required=True)