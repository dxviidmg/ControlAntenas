from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from .forms import *

class ListClientes(View):
	def get(self, request):
		template_name = "clientes/listClientes.html"
		users = User.objects.all().order_by('last_name', 'first_name')
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

		context={
		'user':user,
		'perfil': perfil,
		'direccion': direccion,
		}

		return render(request, template_name, context)

class CreateCliente(View):
	def get(self, request):
		template_name = "clientes/createClienteUser.html"
		form = ClienteForm()
		formdos = PerfilForm()
		context = {
		'form':form,
		'formdos': formdos
		}
		return render(request,template_name,context)