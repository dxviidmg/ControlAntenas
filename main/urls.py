from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(), name="home"),
	url(r'^qs/$', views.QuienesSomos.as_view(), name="qs"),
	url(r'^paquetes/$', views.Paquetes.as_view(), name="paquetes"),
	url(r'^contacto/$', views.Contacto.as_view(), name="contacto"),
]