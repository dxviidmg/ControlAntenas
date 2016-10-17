from django import template 
register = template.Library()
from ..models import Paquete

@register.simple_tag
def paquetes():
	return Paquete.objects.all()