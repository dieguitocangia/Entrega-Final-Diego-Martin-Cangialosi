from django.db import models
from django.http import HttpResponse
from django.template import Template, context
from django.contrib.auth.models import User

# Create your models here.
class Clase(models.Model):
    nombre = models.CharField(max_length=50)
    horario = models.TimeField()
    def __str__(self):
        return f"{self.nombre} - {self.horario}"

class Alumno(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    clase_a_cargo = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    horarios_de_atencion = models.CharField(max_length=200)
    servicios = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.user} [{self.imagen}]"

