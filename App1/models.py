from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Empresa")
    cuit = models.CharField(max_length=20, verbose_name="CUIT de la Empresa")
    area = models.CharField(max_length=50, verbose_name="Area de la empresa")

    def __str__(self):
        return f"Empresa: {self.nombre} - CUIT: {self.cuit} - Area: {self.area}"

class Empleados(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre del empleado")
    apellido = models.CharField(max_length=40, verbose_name="Apellido del empleado")
    cuil = models.CharField(max_length=15, verbose_name="CUIL del empleado")
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    
    def __str__(self):
        return f"Vigilador: {self.nombre} - Apellido: {self.apellido}"

class Servicios(models.Model):
    nombre_servicio = models.CharField(max_length=40, verbose_name="Nombre del Servicio")
    cantidad_empleados = models.IntegerField(default=0)

    def __str__(self):
        return f"Servicio de Seguridad: {self.nombre_servicio} - Empleados: {self.cantidad_empleados}" 


