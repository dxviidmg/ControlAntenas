from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from .forms import *
from servicio.models import *
from infraestructura.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login

class ListClientes(View):
	def get(self, request):
		template_name = "clientes/listClientes.html"
		users = User.objects.all().order_by('last_name', 'first_name').filter(is_superuser=False)
		context = {
			'users': users,
		}
		return render(request, template_name, context)

class DetailCliente(View):
	def get(self, request, pk, redlan=None, celula=None, linea=None):
		template_name="clientes/detailCliente.html"

		user = get_object_or_404(User, pk=pk)
		perfil = get_object_or_404(Perfil, user=user)
		direccion = get_object_or_404(Direccion, perfil=perfil)
		servicio = get_object_or_404(Servicio, user=user)

		if RedLan.objects.filter(servicio=servicio).exists():
			redlan = get_object_or_404(RedLan, servicio=servicio)
		
		if Celula.objects.filter(redlan=redlan):
			celula = get_object_or_404(Celula, redlan=redlan)
		
		if Linea.objects.filter(celula=celula):
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
	@method_decorator(login_required)
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

		ahora = datetime.now()
		dia = ahora.day
		mes = ahora.month

		cuenta = User.objects.filter(is_staff=False).count()
		uactual = cuenta + 1

		nuevo_user_form = UserCreateForm(request.POST)
		nuevo_perfil_form = PerfilForm(request.POST)
		nuevo_domicilio_form = DomicilioForm(request.POST)
		
		if nuevo_user_form.is_valid(): 
			nuevo_user = nuevo_user_form.save(commit=False)
			nuevo_user.username = str(nuevo_user.last_name[0].upper()) + str(nuevo_user.last_name[2].upper()) + str(nuevo_user.first_name[0].upper()) + str(nuevo_user.first_name[1].upper()) + str(dia) + str(mes) + str(uactual)
			nuevo_user.save()

		if nuevo_perfil_form.is_valid():
			nuevo_perfil = nuevo_perfil_form.save(commit=False)
			nuevo_perfil.user = nuevo_user
			nuevo_perfil.save()

		if nuevo_domicilio_form.is_valid():
			nuevo_domicilio = nuevo_domicilio_form.save(commit=False)
			nuevo_domicilio.perfil = nuevo_perfil
			nuevo_domicilio.save()

		return redirect("servicio:createServicio", pk=nuevo_user.pk)

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