from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import *
from django.db.models import Sum
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from servicio.models import *
from .forms import CelulaCreateForm, RedLanCreateForm

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
		form = CelulaCreateForm()
		context = {
			'lineas': lineas,
			'linea': linea,
			'celulas': celulas,
			'form': form,	
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "infraestructura/detailLinea.html"
		nueva_celula_form = CelulaCreateForm(request.POST)
		if nueva_celula_form.is_valid():
			nueva_celula = nueva_celula_form.save(commit=False)
			nueva_celula.linea = Linea.objects.get(pk=pk)
			nueva_celula.save()
		return redirect("infraestructura:detailLineaAndlistCelulas", pk=pk) 

class DetailCelulaAndListLans(View):
	def get(self, request, pk):
		template_name = "infraestructura/detailCelula.html"

		celulas = Celula.objects.all().order_by("ubicacion")
		celula = get_object_or_404(Celula, pk=pk)
		
		redLans = RedLan.objects.all().order_by("ip_red").filter(celula=celula)

		form = RedLanCreateForm()
		context = {
			'celulas': celulas,
			'celula': celula,
			'redLans': redLans,
			'form': form,
		}
		return render(request, template_name, context)
	def post(self,request, pk):
		template_name = "infraestructura/detailCelula.html"
		nueva_redlan_form = RedLanCreateForm(request.POST)
		if nueva_redlan_form.is_valid():
			nueva_redlan = nueva_redlan_form.save(commit=False)
			nueva_redlan.celula = Celula.objects.get(pk=pk)
			nueva_redlan.save()
		return redirect("infraestructura:detailCelulaAndListLans", pk=pk) 

class CreateLinea(CreateView):
	model = Linea
	success_url = reverse_lazy('infraestructura:listLineas')
	fields = ['descripcion', 'distribuidor', 'ancho_de_banda', 'pago', 'fecha_proximo_pago']

class UpdateLinea(UpdateView):
	model = Linea
	success_url = reverse_lazy('infraestructura:listLineas')
	fields = ['descripcion', 'distribuidor', 'ancho_de_banda', 'pago', 'fecha_proximo_pago']

class DeleteLinea(DeleteView):
	model = Linea
	success_url = reverse_lazy('infraestructura:listLineas')