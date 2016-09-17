from django.conf.urls import url
from . import views

urlpatterns = [
 	url(r'^servicios', views.ListServicios.as_view(),name="listServicios"),
  	url(r'^paquetes', views.ListPaquetes.as_view(),name="listPaquetes")
]