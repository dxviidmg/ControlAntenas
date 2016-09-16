from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^lineas/celulas/(?P<pk>[-\w]+)/$', views.DetailCelulaAndListLans.as_view(), name="detailCelulaAndListLans"),
	url(r'^lineas/(?P<pk>[-\w]+)/$', views.DetailLineaAndListCelulas.as_view(), name="detailLineaAndlistCelulas"),
 	url(r'^lineas', views.ListLineas.as_view(),name="listLineas")
]