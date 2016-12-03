from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from servicio.models import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from datetime import date, timedelta, datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

class CreatePagoInstalacion(View):
	@method_decorator(login_required)
	def get(self, request, pk):
		template_name = "pagos/createPagoInstalacion.html"
		nuevopagoinst = PagoInstalacionForm()
		servicio = get_object_or_404(Servicio, pk=pk)
		user = get_object_or_404(User, servicio=servicio)
		context = {
			'nuevopagoinst': nuevopagoinst,
			'user': user,
		}
		return render(request,template_name,context)
	def post(self,request, pk):
		template_name = "pagos/createPagoInstalacion.html"		

		servicio = get_object_or_404(Servicio, pk=pk)
		user = get_object_or_404(User, servicio=servicio)

		nuevo_pago_instalacion_form = PagoInstalacionForm(request.POST)
		if nuevo_pago_instalacion_form.is_valid:
			nuevo_pago_instalacion = nuevo_pago_instalacion_form.save(commit=False)
			nuevo_pago_instalacion.servicio = servicio
			nuevo_pago_instalacion.save()
		return redirect("servicio:listServicios")
#		nuevo_pago_inst = PagoInstalacion()
#		nuevo_pago_inst.servicio = servicio
#		nuevo_pago_inst.monto = 200
#		nuevo_pago_inst.save()
#		return redirect("servicio:listServicios")

#		regresar a detailcliente
#		return redirect("clientes:DetailCliente", pk=user.pk)

class CreatePagoRenta(View):
	@method_decorator(login_required)
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
	@method_decorator(login_required)
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
	@method_decorator(login_required)
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
	@method_decorator(login_required)
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

class CreatePagoRentaUser(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "pagos/createPagoRentaUser.html"

		servicio = get_object_or_404(Servicio, pk=request.user.pk)
		paquete = get_object_or_404(Paquete, servicio=servicio)
		formpagorenta = PagoRentaForm()

		context = {
			'formpagorenta': formpagorenta,
			'paquete': paquete,
		}
		return render(request,template_name,context)
	def post(self,request):
		template_name = "pagos/createPagoRenta.html"		
		
		servicio = get_object_or_404(Servicio, pk=request.user.pk)
		paquete = get_object_or_404(Paquete, servicio=servicio)
		nuevo_pago_renta_form = PagoRentaForm(request.POST)

		if nuevo_pago_renta_form.is_valid():
			nuevo_pago_renta = nuevo_pago_renta_form.save(commit=False)
			nuevo_pago_renta.servicio = servicio
			nuevo_pago_renta.monto = paquete.precio
			nuevo_pago_renta.save()
		return redirect(reverse('pagos:eleccionPago'))

class EleccionPago(View):
	def get(self,request):
#		order_id=request.session.get('order_id')
#		order=get_object_or_404(Orden,id=order_id)
#		host=request.get_host()
#
#		paypal_dict={
#			'business':settings.PAYPAL_RECEIVER_EMAIL,
#			'amount':'%.2f' % order.get_total_cost().quantize(Decimal('.01')),
#			'item_name':'Order {}'.format(order.id),
#			'invoice':str(order.id),
#			'currency_code':'MXN',
#			'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
#			'return_url':'http://{}{}'.format(host,reverse('pagos:donePago')),
#			'cancel_return':'http://{}{}'.format(host,reverse('pagos:canceledPago')),
#		}
#		form=PayPalPaymentsForm(initial=paypal_dict)

		return render(request,'pagos/eleccionPago.html')