from django.shortcuts import render
from django.views.generic import View
from servicio.models import Paquete

class Home(View):
	def get(self, request):
		template_name = 'index.html'
		return render(request, template_name)

class QuienesSomos(View):
	def get(self, request):
		template_name = 'quienessomos.html'
		return render(request, template_name)

class Paquetes(View):
	def get(self, request):
		template_name = 'paquetes.html'
		paquetes = Paquete.objects.all()
		context = {
		'paquetes': paquetes
		}
		return render(request, template_name, context)

class Contacto(View):
	def get(self, request):
		template_name = 'contacto.html'
		return render(request, template_name)