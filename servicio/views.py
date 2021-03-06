from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import *
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ListServicios(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "servicio/listServicios.html"
		servicios = Servicio.objects.all()
		context = {
			'servicios': servicios,
		}
		return render(request, template_name, context)

class ListPaquetes(View):
	@method_decorator(login_required)
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
	fields = ['nombre', 'tipo', 'megas_de_internet', 'precio', 'publicado', 'imagen']

class UpdatePaquete(UpdateView):
	
	model = Paquete
	success_url = reverse_lazy('servicio:listPaquetes')
	fields = ['nombre', 'tipo', 'megas_de_internet','precio', 'publicado', 'imagen']

class DeletePaquete(DeleteView):
	
	model = Paquete
	success_url = reverse_lazy('servicio:listPaquetes')

class CreateServicio(View):
	
	def get(self, request, pk):
		template_name = "servicio/createServicio.html"
		formservicio = ServicioForm()
		user = get_object_or_404(User, pk=pk)
		context = {
			'formservicio': formservicio,
			'pk': pk,
			'user': user,
		}
		return render(request,template_name,context)
	def post(self,request, pk):
		
		user = get_object_or_404(User, pk=pk)

		template_name = "servicio/createServicio.html"
		nuevo_servicio_form = ServicioForm(request.POST)
		if nuevo_servicio_form.is_valid():
			nuevo_servicio = nuevo_servicio_form.save(commit=False)
			nuevo_servicio.user = user
			nuevo_servicio.save()
		return redirect("pagos:createPagoInstalacion", pk=nuevo_servicio.pk)

class UpdateServicio(UpdateView):
	
	model = Servicio
	success_url = reverse_lazy('servicio:listServicios')
	fields = ['user', 'paquete', 'estado', 'inicio_de_servicio' ]

class DeleteServicio(DeleteView):
	
	model = Servicio
	success_url = reverse_lazy('servicio:listServicios')

