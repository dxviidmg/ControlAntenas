from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^lineas/celulas/(?P<pk>[-\w]+)/$', views.DetailCelulaAndListLans.as_view(), name="detailCelulaAndListLans"),

	url(r'^lineas/actualizar/(?P<pk>\d+)/$', views.UpdateLinea.as_view(), name="updateLinea"),
	url(r'^lineas/nuevo/$', views.CreateLinea.as_view(), name="createLinea"),
	url(r'^lineas/borrar/(?P<pk>\d+)/$', views.DeleteLinea.as_view(), name="deleteLinea"),
	url(r'^lineas/(?P<pk>[-\w]+)/$', views.DetailLineaAndListCelulas.as_view(), name="detailLineaAndlistCelulas"),
 	url(r'^lineas', views.ListLineas.as_view(),name="listLineas")
]