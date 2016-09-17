from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

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

class CreatePaquete(CreateView):
	model = Paquete
	success_url = reverse_lazy('servicio:listPaquetes')
	fields = ['nombre', 'descripcion', 'precio']

class UpdatePaquete(UpdateView):
	model = Paquete
	success_url = reverse_lazy('servicio:listPaquetes')
	fields = ['nombre', 'descripcion', 'precio']

class DeletePaquete(DeleteView):
	model = Paquete
	success_url = reverse_lazy('servicio:listPaquetes')