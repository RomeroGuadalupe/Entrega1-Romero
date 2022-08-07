from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre = models.CharField (max_length=150)
    apellido = models.CharField (max_length=150)
    telefono = models.IntegerField (blank=True , null=True)
    direccion = models.CharField (max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

