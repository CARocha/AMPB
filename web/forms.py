from django import forms

class BuscadorForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(BuscadorForm, self).__init__(*args, **kwargs)
		self.fields['q'] = forms.CharField()


class ContactoForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ContactoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'] = forms.CharField(required = True)
		self.fields['correo'] = forms.EmailField(required = True)
		self.fields['telefono'] = forms.CharField(required = True)
		self.fields['asunto'] = forms.CharField(required = True)
		self.fields['mensaje'] = forms.CharField(widget=forms.Textarea, required=True)
