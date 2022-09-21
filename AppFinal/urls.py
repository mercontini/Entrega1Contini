from django.urls import path
from AppFinal.views import *
from AppFinal import views


urlpatterns = [
   
    path('', inicio, name="Inicio"), 
    path("destino/", views.destino , name = "Destino"),
    path("actividades/", views.actividades , name = "Actividades"),
    path("traslados/", views.traslados , name = "Traslados"),
    path("contacto/", views.contacto , name = "Contacto"),
    path('busquedas',views.busqueda,name="Busqueda Reseñas"),
    path('resultadobusqueda',views.resultadobusqueda,name="Resultado Busqueda"),
    path('buscar/', views.buscar),

      
]

