from django.db import models
from django.contrib.auth.models import User

class Paquete(models.Model):

	Nombre_CHOICES = (
		('Institucional', (
				('10 Megas', '10 Megas'),
				('20 Megas', '20 Megas'),
			)
		),
		('Familiar', (
			('Triple Play 5 Megas', 'Triple Play 5 Megas'),
				('Triple Play 5 Megas', 'Triple Play 3 Megas'),
			)
		),
	)
	nombre = models.CharField(max_length=30, choices=Nombre_CHOICES)
	descripcion = models.CharField(max_length=100)
	megas_de_internet = models.IntegerField()
	precio = models.IntegerField()

	def __str__(self):
		return self.nombre

class Servicio(models.Model):

	Estado_CHOICES = (
		('Proceso de alta', (
				('Pendiente instalar la antena', 'Pendiente instalar la antena'),
			)
		),
		('En servicio', (
			('Activo', 'Activo'),
			('Suspendido', 'Suspendido'),
			)
		),
		('Proceso de Baja', (
			('Pendiente ir por la antena', 'Pendiente ir por la antena'),
			('Baja definitiva', 'Baja definitiva'),
			)
		),
	)

	user = models.OneToOneField(User)
	fecha_de_inicio_de_servicio = models.DateField(null=True, blank=True)
	paquete = models.ManyToManyField(Paquete)
	estado = models.CharField(max_length=30, choices=Estado_CHOICES)

	def __str__(self):
		return '{}'.format(self.user.username)