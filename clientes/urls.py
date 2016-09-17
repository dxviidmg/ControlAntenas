from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, logout_then_login

urlpatterns = [

	url(r'^cliente/registro/$', views.CreateCliente.as_view(), name="createCliente"),
	url(r"^clientes/(?P<pk>\d+)/$", views.DetailCliente.as_view(), name="detailCliente"),
 	url(r'^clientes', views.ListClientes.as_view(),name="listClientes"),
 	url(r'^login/$', login, name="login"),
]