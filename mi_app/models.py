from django.db import models

from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Cita(models.Model):
    cliente =  models.ForeignKey(Cliente , on_delete=models.CASCADE, related_name =  'citas')
    fecha_cita = models.DateTimeField()
    motivo = models.CharField(max_length=50)

    def __str__(self):
        return f"Cita de {self.cliente.nombre} el {self.fecha_cita}"
  

# Create your models here.
