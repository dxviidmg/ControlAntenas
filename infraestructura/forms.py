from django import forms
from .models import Celula

class CelulaCreateForm(forms.ModelForm):
	class Meta:
		model =Celula
		fields =[
			'ubicacion','ancho_de_banda',]
