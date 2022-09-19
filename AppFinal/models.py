from django.db import models

# Create your models here.

class Destino(models.Model):
    provincia = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    codigopostal = models.IntegerField()

class Actividades(models.Model):
    tipo = models.CharField(max_length=30)
    modalidad = models.CharField(max_length=30)
    duracion = models.IntegerField()

class Traslados(models.Model):
    tipo= models.CharField(max_length=30)
    duracion = models.IntegerField()

