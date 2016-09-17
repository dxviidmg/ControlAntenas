from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^servicios/nuevo/$', views.CreateServicio.as_view(), name="createServicio"),
 	url(r'^servicios/actualizar/(?P<pk>\d+)/$', views.UpdateServicio.as_view(), name="updateServicio"),
	url(r'^servicios/borrar/(?P<pk>\d+)/$', views.DeleteServicio.as_view(), name="deleteServicio"),
 	url(r'^servicios', views.ListServicios.as_view(),name="listServicios"),

	url(r'^paquetes/nuevo/$', views.CreatePaquete.as_view(), name="createPaquete"),
 	url(r'^paquetes/actualizar/(?P<pk>\d+)/$', views.UpdatePaquete.as_view(), name="updatePaquete"),
	url(r'^paquetes/borrar/(?P<pk>\d+)/$', views.DeletePaquete.as_view(), name="deletePaquete"),
  	url(r'^paquetes', views.ListPaquetes.as_view(),name="listPaquetes")
]