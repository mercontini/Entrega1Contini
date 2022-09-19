from django.shortcuts import render
from AppFinal.models import *
# Create your views here.

def inicio (request):
    return render(request, "AppFinal/inicio.html")
