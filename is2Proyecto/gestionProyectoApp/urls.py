from gestionProyectoApp import views
from django.urls import path

urlpatterns = [
	path('', views.login), 
	path('homeProyecto/', views.iniciarSesion)
]