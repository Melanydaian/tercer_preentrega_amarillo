from django.contrib import admin
from .models import Empresa, Empleados, Servicios


# Register your models here.
admin.site.register(Empresa)
admin.site.register(Empleados)
admin.site.register(Servicios)
