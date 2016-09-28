from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from .forms import *
from servicio.models import *
from infraestructura.models import *

class ListClientes(View):
	def get(self, request):
		template_name = "clientes/listClientes.html"
		users = User.objects.all().order_by('last_name', 'first_name').filter(is_superuser=False)
		context = {
		'users': users,
		}
		return render(request, template_name, context)

class DetailCliente(View):
	def get(self, request, pk):
		template_name="clientes/detailCliente.html"
		user = get_object_or_404(User, pk=pk)
		perfil = get_object_or_404(Perfil, user=user)
		direccion = get_object_or_404(Direccion, perfil=perfil)
		servicio = get_object_or_404(Servicio, user=user)
		redlan = get_object_or_404(RedLan, servicio=servicio)
		celula = get_object_or_404(Celula, redlan=redlan)
		linea = get_object_or_404(Linea, celula=celula)

		context={
		'user':user,
		'perfil': perfil,
		'direccion': direccion,
		'servicio': servicio,
		'redlan': redlan,
		'celula': celula,
		'linea': linea,
		}

		return render(request, template_name, context)

class CreateCliente(View):
	def get(self, request):
		template_name = "clientes/createCliente.html"
		form = UserCreateForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "clientes/createCliente.html"
		nuevo_user_form = UserCreateForm(request.POST)
		if nuevo_user_form.is_valid():
			nuevo_user = nuevo_user_form.save(commit=False)
			nuevo_user.save()
			#perfil = Perfil()
			#perfil.user = nuevo_user
			#perfil.save()
		return redirect("clientes:listClientes") 