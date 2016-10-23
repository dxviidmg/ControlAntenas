from django import template 
register = template.Library()
from ..models import Empresa

@register.simple_tag
def datosempresa():
	return Empresa.objects.all()