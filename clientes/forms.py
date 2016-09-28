from django import forms
from django.contrib.auth.models import User
from .models import *

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('telefono',)

class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ('calle', 'numero_exterior', 'numero_interior', 'colonia', 'municipio', 'estado', 'codigo_postal',)