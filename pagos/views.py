from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from servicio.models import *
from .models import *
from .forms import *
from django.contrib.auth.models import User

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
		#Ultimo pago de cada usuario
		pagos = PagoRenta.objects.all().order_by("servicio")
		
		context = {
			'pagos': pagos,
		}
		return render(request, template_name, context)