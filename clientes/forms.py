from django import forms
from django.contrib.auth.models import User
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('telefono',)

class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ('calle', 'numero_exterior', 'numero_interior', 'colonia', 'municipio', 'estado', 'codigo_postal',)