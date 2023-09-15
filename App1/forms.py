from django import forms


class EmpresaFormulario(forms.Form):
    nombre = forms.CharField(max_length=70, label="Nombre")
    cuit = forms.IntegerField(label="CUIT")
    area = forms.CharField(max_length=50 , label="Area")
    
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=70, label="Nombre")
    apellido = forms.CharField(max_length=70, label="Apellido")
    cuil = forms.IntegerField(label="CUIL")
    fecha_ingreso = forms.DateField(label="Fecha de Ingreso")
   

class ServiciosFormulario(forms.Form):
    nombre_servicio = forms.CharField(max_length=40, label="Servicio")

