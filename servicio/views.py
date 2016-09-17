from django.shortcuts import render
from django.views.generic import View
from .models import *

class ListServicios(View):
	def get(self, request):
		template_name = "servicio/listServicios.html"
		servicios = Servicio.objects.all()
		context = {
			'servicios': servicios,
		}
		return render(request, template_name, context)

class ListPaquetes(View):
	def get(self, request):
		template_name = "servicio/listPaquetes.html"
		paquetes = Paquete.objects.all()
		context = {
			'paquetes': paquetes,
		}
		return render(request, template_name, context)