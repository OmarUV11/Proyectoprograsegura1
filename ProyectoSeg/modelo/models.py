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
      Chat_id = models.CharField(max_length = 40, null=True)
      Token_tel = models.CharField(max_length = 60, null=True)
      Token_Env = models.CharField(max_length = 60, null=True)     
      Token_Tem = models.DateTimeField(null=True)
      salt = models.CharField(max_length = 16, default="", null=True )

class IntentosIP(models.Model):
      ip = models.GenericIPAddressField(unique=True, null=True)
      intentos = models.IntegerField(default=1)
      timestamp = models.DateTimeField(null=True)

      
