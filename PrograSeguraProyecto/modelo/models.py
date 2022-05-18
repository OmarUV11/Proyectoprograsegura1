from django.db import models

# Create your models here.
class Usuario(models.Model):
      nombre = models.CharField(max_length = 25)
      contraseña = models.CharField(max_length = 100)
      
class Alumnos(models.Model):
      NombreAlumno = models.CharField(max_length = 50)
      Matricula =  models.CharField(max_length = 20)
      Contraseña = models.CharField(max_length = 20)
      Tipocuenta = models.CharField(max_length = 20, null=True)
