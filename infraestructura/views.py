from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.db.models import Sum

class ListLineas(View):
	def get(self, request):
		template_name = "infraestructura/listLineas.html"
		lineas = Linea.objects.all().order_by("descripcion")
		context = {
			'lineas': lineas,
		}
		return render(request, template_name, context)

class DetailLineaAndListCelulas(View):
	def get(self, request, pk):
		template_name = "infraestructura/detailLinea.html"
		lineas = Linea.objects.all().order_by("descripcion")
		linea = get_object_or_404(Linea, pk=pk)
		celulas = Celula.objects.all().order_by("ubicacion").filter(linea=linea)

		context = {
			'lineas': lineas,
			'linea': linea,
			'celulas': celulas,
			
		}
		return render(request, template_name, context)

class DetailCelulaAndListLans(View):
	def get(self, request, pk):
		template_name = "infraestructura/detailCelula.html"
		celulas = Celula.objects.all().order_by("ubicacion")
		celula = get_object_or_404(Celula, pk=pk)
		redes = RedLan.objects.all().order_by("ip_red").filter(celula=celula)
		

		context = {
			'celula': celula,
			'redes': redes,
			'celulas': celulas,
		}
		return render(request, template_name, context)