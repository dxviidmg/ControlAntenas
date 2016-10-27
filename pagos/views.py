from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from servicio.models import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from datetime import date, timedelta, datetime

class CreatePagoInstalacion(View):
	def get(self, request, pk):
		template_name = "pagos/createPagoInstalacion.html"
		servicio = get_object_or_404(Servicio, pk=pk)
		user = get_object_or_404(User, servicio=servicio)
		context = {
			'user': user,
		}
		return render(request,template_name,context)
	def post(self,request, pk):
		template_name = "pagos/createPagoInstalacion.html"		

		servicio = get_object_or_404(Servicio, pk=pk)
		user = get_object_or_404(User, servicio=servicio)

		nuevo_pago_inst = PagoInstalacion()
		nuevo_pago_inst.servicio = servicio
		nuevo_pago_inst.monto = 200
		nuevo_pago_inst.save()
		return redirect("servicio:listServicios")
#		regresar a detailcliente
#		return redirect("clientes:DetailCliente", pk=user.pk)

class CreatePagoRenta(View):
	def get(self, request, pk):
		template_name = "pagos/createPagoRenta.html"

		servicio = get_object_or_404(Servicio, pk=pk)
		paquete = get_object_or_404(Paquete, servicio=servicio)
		formpagorenta = PagoRentaForm()

		context = {
			'formpagorenta': formpagorenta,
			'pk': pk,
			'paquete': paquete,
		}
		return render(request,template_name,context)
	def post(self,request, pk):
		template_name = "pagos/createPagoRenta.html"		
		
		servicio = get_object_or_404(Servicio, pk=pk)
		paquete = get_object_or_404(Paquete, servicio=servicio)

		nuevo_pago_renta_form = PagoRentaForm(request.POST)
		if nuevo_pago_renta_form.is_valid():
			nuevo_pago_renta = nuevo_pago_renta_form.save(commit=False)
			nuevo_pago_renta.servicio = servicio
			nuevo_pago_renta.monto = paquete.precio
			nuevo_pago_renta.save()
		return redirect("servicio:listServicios")

class Historial(View):
	def get(self, request, pk):
		template_name = "pagos/historial.html"

		servicio = get_object_or_404(Servicio, pk=pk)

		pagosRenta = PagoRenta.objects.all().filter(servicio=servicio).order_by("año", "mes")
		pagoInstalacion = get_object_or_404(PagoInstalacion, servicio=servicio)
		pagos = PagoRenta.objects.all().filter(servicio=servicio)
		context = {
			'pagosRenta': pagosRenta,
			'pagoInstalacion': pagoInstalacion
		}
		return render(request,template_name,context)

class ListUltimosPagos(View):
	def get(self, request):
		template_name = "pagos/ultimospagos.html"
		
		#Hacer reporte
		servicios = Servicio.objects.all()
		ultimospagos = []
		for servicio in servicios:
			ultimospagos.append({'pago':PagoRenta.objects.all().filter(servicio=servicio).last()}) 
		
		pagos = PagoRenta.objects.all().order_by("servicio")
		
		context = {
			'pagos': pagos,
			'ultimospagos': ultimospagos,
		}
		return render(request, template_name, context)

class ListPagosPorMes(View):
	def get(self, request):
		template_name="pagos/reportepagospormes.html"
		hoy = date.today()
		pagosrenta = PagoRenta.objects.all().order_by("fecha")
		pagosinstalacion = PagoInstalacion.objects.all().order_by("fecha")
		
		ahora = datetime.now()
		primerodelmes = date.today() - timedelta(days=ahora.day-1)

		pagosrentahechos = []
		pagosinstalacionhechos = []
		
		totalpagorenta = 0
		for pagorenta in pagosrenta:
			if pagorenta.fecha >= primerodelmes and pagorenta.fecha <= hoy:
				pagosrentahechos.append(pagorenta)
				totalpagorenta = totalpagorenta + pagorenta.monto

		totalpagoinstalacion = 0
		for pagoinstalacion in pagosinstalacion:
			if pagoinstalacion.fecha <= hoy:
				pagosinstalacionhechos.append(pagoinstalacion)
				totalpagoinstalacion = totalpagoinstalacion + pagoinstalacion.monto
		sumadepagos = totalpagorenta + totalpagoinstalacion
		context = {
			'pagosinstalacionhechos': pagosinstalacionhechos,
			'pagosrentahechos':pagosrentahechos,
			'sumadepagos': sumadepagos,
			'primerodelmes': primerodelmes,
			}
		return render(request, template_name, context)