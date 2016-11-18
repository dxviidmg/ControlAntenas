from django import template 
register = template.Library()
from ..models import Paquete

@register.simple_tag
def paquetesFamiliares():
	return Paquete.objects.filter(publicado=True, tipo="Familiar")

@register.simple_tag
def paquetesInstitucionales():
	return Paquete.objects.filter(publicado=True, tipo="Institucional")

