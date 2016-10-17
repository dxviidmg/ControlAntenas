from django.db import models
from django.contrib.auth.models import User

class Paquete(models.Model):

	Tipo_CHOICES = (
	    ('Familiar', 'Familiar'),
	    ('Institucional', 'Institucional'),
	)

	nombre = models.CharField(max_length=30)
	tipo = models.CharField(max_length=20, choices=Tipo_CHOICES, null=True, blank=True)
	descripcion = models.CharField(max_length=100)
	megas_de_internet = models.IntegerField()
	precio = models.IntegerField()
	imagen = models.ImageField(upload_to='paquetes', null=True, blank=True)

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
	inicio_de_servicio = models.DateField(null=True, blank=True)
	paquete = models.ForeignKey(Paquete)
	estado = models.CharField(max_length=30, choices=Estado_CHOICES)

	def __str__(self):
		return '{}'.format(self.user.username)