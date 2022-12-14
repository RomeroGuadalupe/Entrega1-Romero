from django.db import models

# Create your models here.
class Productos (models.Model):
    nombre = models.CharField (max_length=150)
    modelo = models.CharField (max_length=150, blank=True , null=True)
    precio = models.IntegerField (default=0)
    

    def __str__(self):
        return f"{self.nombre} - {self.modelo}"


class Integrantes (models.Model):
    nombre = models.CharField (max_length=150)
    edad = models.IntegerField ()
    profesion = models.CharField(max_length=150)
    
    def __str__(self):
     return f"informacion de {self.nombre}"

class Sucursales (models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    dias = models.CharField(max_length=150)
    horarios = models.CharField(max_length=150) 

    def __str__(self):
     return f"Sucursal {self.nombre}"

