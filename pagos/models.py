from django.db import models
from servicio.models import Servicio
from django.utils import timezone

class PagoInstalacion(models.Model):
	servicio = models.OneToOneField(Servicio)
	monto = models.IntegerField()
	fecha = models.DateField(default=timezone.now)
	hora = models.TimeField(default=timezone.now)
	def __str__(self):
		return 'Instalación de {}'.format(self.servicio, )

class PagoRenta(models.Model):
	Mes_CHOICES = (
		(1 , 'Enero'),
		(2 , 'Febrero'),
		(3 , 'Marzo'),
		(4 , 'Abril'),
		(5 , 'Mayo'),
		(6 , 'Junio'),
		(7 , 'Julio'),
		(8 , 'Agosto'),
		(9 , 'Septiembre'),
		(10 , 'Octubre'),
		(11 , 'Noviembre'),
		(12 , 'Diciembre'),
	)
	servicio = models.ForeignKey(Servicio)
	mes = models.IntegerField(choices=Mes_CHOICES)
	año = models.IntegerField()
	monto = models.IntegerField()
	fecha = models.DateField(default=timezone.now)
	hora = models.TimeField(default=timezone.now)

	def __str__(self):
		return 'Mensualidad de {} del mes {} del año {}'.format(self.servicio, self.mes, self.año)