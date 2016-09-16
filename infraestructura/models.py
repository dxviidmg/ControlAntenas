from django.db import models
from servicio.models import Servicio

class Linea(models.Model):
	descripcion = models.CharField(max_length=100)
	distribuidor = models.CharField(max_length=20)
	ancho_de_banda = models.IntegerField()
	pago = models.IntegerField(blank=True,null=True)
	fecha_proximo_pago = models.DateField(blank=True,null=True)

	def __str__(self):
		return self.descripcion

class Celula(models.Model):
	ubicacion = models.CharField(max_length=100)
	ancho_de_banda = models.IntegerField()
	linea = models.ForeignKey(Linea)

	def __str__(self):
		return self.ubicacion

class RedLan(models.Model):
	ip_red = models.GenericIPAddressField()
	ip_host_inicial = models.GenericIPAddressField()
	ip_host_final = models.GenericIPAddressField()
	ip_mascara_de_red = models.GenericIPAddressField()
	celula = models.ForeignKey(Celula)
	servicio = models.OneToOneField(Servicio, blank=True,null=True)

	def __str__(self):
		return self.ip_red