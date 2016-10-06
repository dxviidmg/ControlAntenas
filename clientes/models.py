from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=10)
	fecha_de_nacimiento = models.DateField(blank=True, null=True)

	def __str__(self):
		return '{}'.format(self.user)

class Direccion(models.Model):
	perfil = models.OneToOneField(Perfil)
	calle = models.CharField(max_length=20)
	numero_exterior = models.CharField(max_length=10)
	numero_interior = models.CharField(max_length=10, blank=True, null=True)
	colonia = models.CharField(max_length=20)
	municipio = models.CharField(max_length=20)
	estado = models.CharField(max_length=20)
	codigo_postal = models.CharField(max_length=5)

	def __str__(self):
		return '{} {} {} {} {}'.format(self.calle, self.numero_exterior, self.numero_interior,
			self.colonia, self.municipio)
	
# Create your models here.
