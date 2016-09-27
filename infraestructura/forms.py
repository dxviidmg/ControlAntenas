from django import forms
from .models import Celula, RedLan

class CelulaCreateForm(forms.ModelForm):
	class Meta:
		model =Celula
		fields =['ubicacion','ancho_de_banda',]

class RedLanCreateForm(forms.ModelForm):
	class Meta:
		model =RedLan
		fields =['ip_red','ip_host_inicial', 'ip_host_final', 'ip_mascara_de_red', 'servicio']