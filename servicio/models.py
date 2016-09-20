from django.db import models
from django.contrib.auth.models import User

class Paquete(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=50)
	precio = models.IntegerField()

	def __str__(self):
		return self.nombre

class Servicio(models.Model):

	STATE_CHOICES = (
        ('Suspendido', 'Suspendido'),
        ('Activado', 'Activado'),
    )

	fecha = models.DateField(auto_now=True)
	user = models.OneToOneField(User)
	paquete = models.ManyToManyField(Paquete)
	estado = models.CharField(max_length=20, choices=STATE_CHOICES)

	def __str__(self):
		return '{}'.format(self.user.username)