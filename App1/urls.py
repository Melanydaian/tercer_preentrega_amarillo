from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('empresa/',views.empresa, name="empresa"),
    path('empleados/',views.empleados, name="empleados"),
    path('servicios/',views.servicios, name="servicios"),
    path('empresaForm/', views.empresaForm, name='EmpresaForm'),
    path('empleadosForm/',views.empleadosForm, name="empleadosForm"),
    path('ServForm/', views.ServForm, name="ServForm"),
    path('encontrarempleados/', views.buscarEmpleados, name="buscarempleado"),
    path('buscar/',views.buscar, name="Buscar"),
]