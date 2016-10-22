from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^administracion/pagos/ultimospagos/$', views.ListUltimosPagos.as_view(), name="listUltimosPagos"),
	url(r'^administracion/pagos/historial/(?P<pk>\d+)/$', views.Historial.as_view(), name="historial"),
	url(r'^administracion/pagos/nuevo/instalacion/(?P<pk>\d+)/$', views.CreatePagoInstalacion.as_view(), name="createPagoInstalacion"),
	url(r'^administracion/pagos/nuevo/renta/(?P<pk>\d+)/$', views.CreatePagoRenta.as_view(), name="createPagoRenta"),
 ]