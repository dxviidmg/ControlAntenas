from django.db import models
from django.contrib.auth.models import User

class Paquete(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=50)
	precio = models.IntegerField()

	def __str__(self):
		return self.nombre

class Servicio(models.Model):
	fecha = models.DateField()
	user = models.OneToOneField(User)
	paquete = models.ManyToManyField(Paquete)

	def __str__(self):
		return '{}'.format(self.pk)