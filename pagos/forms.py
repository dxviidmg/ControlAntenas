from django import forms
from .models import *

class PagoRentaForm(forms.ModelForm):
    class Meta:
        model = PagoRenta
        fields = ( 'mes','año')

class PagoInstalacionForm(forms.ModelForm):
    class Meta:
        model = PagoInstalacion
        fields = ('monto',)