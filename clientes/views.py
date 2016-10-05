from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from .forms import *
from servicio.models import *
from infraestructura.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ListClientes(View):
	def get(self, request):
		template_name = "clientes/listClientes.html"
		users = User.objects.all().order_by('last_name', 'first_name').filter(is_superuser=False)
		context = {
		'users': users,
		}
		return render(request, template_name, context)

class DetailCliente(View):
	def get(self, request, pk, servicio=None, redlan=None, celula=None, linea=None):
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
		formuser = UserCreateForm()
		formperfil = PerfilForm()
		formdomicilio = DomicilioForm()
		context = {
		'formuser':formuser,
		'formperfil': formperfil,
		'formdomicilio': formdomicilio,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "clientes/createCliente.html"
		nuevo_user_form = UserCreateForm(request.POST)
		nuevo_perfil_form = PerfilForm(request.POST)
		nuevo_domicilio_form = DomicilioForm(request.POST)
		if nuevo_user_form.is_valid() and nuevo_perfil_form.is_valid() and nuevo_domicilio_form.is_valid():
			nuevo_user = nuevo_user_form.save(commit=False)
			nuevo_user.save()

			nuevo_perfil = Perfil()
			nuevo_perfil.user = nuevo_user
			nuevo_perfil.save()

			nuevo_domicilio = Direccion()
			nuevo_domicilio.perfil = nuevo_perfil
			nuevo_domicilio.save()
		return redirect("clientes:listClientes")


from django.contrib.auth import authenticate, login

def login_user(request):

	template_name="registration/login.html"

	username = request.POST.get("username", False)
	password = request.POST.get("password", False)
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_staff:
			login(request, user)
			return redirect("infraestructura:listLineas")
		else:
			login(request, user)
			return redirect("clientes:bienvenido")
	else:
		return render(request,template_name)



class Bienvenido(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="clientes/bienvenido.html"
		userform = UserCreateForm(instance=request.user)
		
		context = {
		'userform':userform,
		}
		return render(request,template_name,context)