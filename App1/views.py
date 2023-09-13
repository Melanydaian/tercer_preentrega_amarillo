from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import *
from .forms import *


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def empresa(request):
    empresa_seguridad=Empresa.objects.all()
    return render(request, "empresa_seguridad.html", {"empresa_seguridad":empresa_seguridad})

def empleados(request):
    listaEmpleados=Empleados.objects.all()
    return render(request, "listaEmpleados.html", {"listaEmpleados":listaEmpleados})

def servicios(request):
    lista_servicios = Servicios.objects.all()
    print(lista_servicios)  
    return render(request, "listaServicios.html", {"lista_servicios": lista_servicios})



def empresaForm(request):
    if request.method == "POST":
        formulario_empresa = EmpresaFormulario(request.POST)
        if  formulario_empresa.is_valid():
            data=formulario_empresa.cleaned_data
            empresa=Empresa(nombre=data["nombre"], cuit=data["cuit"], area=data["area"])
            empresa.save()
            return render(request, "inicio.html")
    else:
        formulario_empresa = EmpresaFormulario()
        return render(request, "formulario_empresa.html", {"formulario_empresa": formulario_empresa})



def empleadosForm(request):
    if request.method == "POST":
        emplForm = EmpleadoFormulario(request.POST)
        if emplForm.is_valid():
            data = emplForm.cleaned_data
            empleados = Empleados(nombre=data["nombre"], apellido=data["apellido"], cuil=data["cuil"], fecha_ingreso=data["fecha_ingreso"])
            empleados.save()
            return render(request, "inicio.html")
    else:
        emplForm = EmpleadoFormulario()
        return render(request, "empleadosForm.html", {"emplForm": emplForm})

    
def ServForm(request):
    if request.method == "POST":
        serv_form = ServiciosFormulario(request.POST)
        if serv_form.is_valid():
            data = serv_form.cleaned_data
            servicio = Servicios(nombre_servicio=data["nombre_servicio"])  # Usar el nombre correcto del campo
            servicio.save()
            return render(request, "inicio.html")
    else:
        serv_form = ServiciosFormulario()
        return render(request, "serviciosForm.html", {"serv_Form": serv_form})


def buscarEmpleados(request):
    nombre = request.GET.get('buscar_nombre', '')  # Obtén el parámetro de búsqueda o una cadena vacía si no se proporciona
    empleados = Empleados.objects.filter(nombre__icontains=nombre)
    if nombre:
        return render(request, "encontrarempleados.html", {"empleado": empleados})

    return render(request, "encontrarempleados.html")

def buscar(request):
    empleados = Empleados.objects.all()
    nombre = request.GET.get('busca_nombre', '')  # Obtén el parámetro de búsqueda o una cadena vacía si no se proporciona

    if nombre:
        empleado = empleados.filter(nombre__icontains=nombre)
    else:
        empleado = []

    return render(request, "encontrarempleados.html", {"empleado": empleado, "empleados": empleados})
