from django.shortcuts import render
from AppFinal.models import *
from django.http import HttpResponse
from AppFinal.models import Destino, Traslados, Actividades
from AppFinal.forms import FormDestino, FormTraslado, FormActividades

# Create your views here.

def inicio (request):
    return render(request, "AppFinal/inicio.html")
    inicio.save()

def destino(request):
    if request.method == "POST":
        DestinoFormulario = FormDestino(request.POST)
        print(DestinoFormulario)
        if DestinoFormulario.is_valid:
            informacion = DestinoFormulario.cleaned_data
            destino=Destino(provincia=informacion['provincia'],ciudad=informacion['ciudad'],codigopostal=informacion['codigopostal'])
            destino.save()
            return render(request,"AppFinal/inicio.html")
    else:
        DestinoFormulario = FormDestino()
    return render(request,"AppFinal/destino.html",{"DestinoFormulario":DestinoFormulario})
    return render(request,"AppFinal/destino.html")

    
def actividades(request):
    if request.method == "POST":
        ActividadFormulario = FormActividades(request.POST)
        print(ActividadFormulario)
        if ActividadFormulario.is_valid:
            informacion = ActividadFormulario.cleaned_data
            actividades=Actividades(tipo=informacion['tipo'],modalidad=informacion['modalidad'],duracion=informacion['duracion'])
            actividades.save()
            return render(request,"AppFinal/inicio.html")
    else:
        ActividadFormulario = FormActividades()
    return render(request,"AppFinal/actividades.html",{"ActividadFormulario":ActividadFormulario})
    return render(request,"AppFinal/actividades.html")


def traslados(request):
    if request.method == "POST":
        TrasladoFormulario = FormTraslado(request.POST)
        print(TrasladoFormulario)
        if TrasladoFormulario.is_valid:
            informacion = TrasladoFormulario.cleaned_data
            traslados=Traslados(tipo=informacion['tipo'],duracion=informacion['duracion'])
            traslados.save()
            return render(request,"AppFinal/inicio.html")
    else:
        TrasladoFormulario = FormTraslado()
    return render(request,"AppFinal/traslados.html",{"TrasladoFormulario":TrasladoFormulario})
    return render(request,"AppFinal/traslados.html")

def contacto(request):
    return render(request, "AppFinal/contacto.html")

def email(request):
    if request.method == "POST":
        EmailFormulario = FormEmail(request.POST)
        print(EmailFormulario)
        if EmailFormulario.is_valid:
            informacion = EmailFormulario.cleaned_data
            email=email(email=informacion['email'])
            email.save()
            return render(request,"AppFinal/inicio.html")
    else:
        EmailFormulario = FormEmail()
    return render(request,"AppFinal/inicio.html",{"EmailFormulario":EmailFormulario})
    return render(request,"AppFinal/inicio.html")

def buscar(request):
    if request.GET['provincia']:
        provincia = request.GET['provincia']
        ciudad = Destino.objects.filter(provincia__icontains= provincia)
        return render(request,"AppFinal/resultadobusqueda.html",{"provincia":provincia, "ciudad":ciudad})
    else:
        respuesta = "No enviaste datos"
    return render(request,"AppFinal/resultadobusqueda.html",{"respuesta":respuesta})

def busqueda(request):
    return render(request,"AppFinal/busqueda.html")

def resultadobusqueda(request):
    return render(request,"AppFinal/resultadobusqueda.html")




