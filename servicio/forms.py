from django import forms
from .models import *

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ('paquete', 'estado',)

