#encoding:utf-8
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset

class PeticionesForm(forms.Form):
	nombre = forms.CharField(
		label="Nombre:",
		max_length=80, 
		required=True,
	)

	ciudad = forms.CharField(
		label="Ciudad:", 
		max_length=80, 
		required=True,
	)
	correo = forms.EmailField(
		label = "Correo:",
		required = True,
	)
	peticion = forms.CharField(
		label = "",
		widget = forms.Textarea,
	)

	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.form_id = 'form-peticion'
		self.helper.form_class = 'uniForm'
		self.helper.form_method = 'post'
		#self.helper.form_action = '/peticiones'

		self.helper.add_input(Submit('submit', 'Enviar'))
		self.helper.add_input(Reset('reset', 'Borrar'))
		super(PeticionesForm, self).__init__(*args, **kwargs)
