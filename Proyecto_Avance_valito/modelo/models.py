from django.db import models
from django.conf import settings

# Create your models here.
class Usuario(models.Model):
      nombre = models.CharField(max_length = 25)
      contraseña = models.CharField(max_length = 100)


class Profesor(models.Model):
      NombreProfesor = models.CharField(max_length = 50)
      Matricula =  models.CharField(max_length = 20)
      Contraseña = models.CharField(max_length = 100)
      Tipocuenta = models.CharField(max_length = 20, null=True)
      Chat_id = models.CharField(max_length = 40, null=True)
      Token_tel = models.CharField(max_length = 60, null=True)
      Token_Env = models.CharField(max_length = 60, null=True)
      Token_Tem = models.DateTimeField(null=True)
      salt = models.CharField(max_length = 100, default="", null=True )
      Estado_token = models.CharField(max_length = 30 , null=True)

class Alumnos(models.Model):
      NombreAlumno = models.CharField(max_length = 50)
      Matricula =  models.CharField(max_length = 20)
      Contraseña = models.CharField(max_length = 100)
      Tipocuenta = models.CharField(max_length = 20, null=True)
      Chat_id = models.CharField(max_length = 40, null=True)
      Token_tel = models.CharField(max_length = 60, null=True)
      Token_Env = models.CharField(max_length = 60, null=True)
      Token_Tem = models.DateTimeField(null=True)
      salt = models.CharField(max_length = 100, default="", null=True )
      Estado_token = models.CharField(max_length = 30 , null=True)


class IntentosIP(models.Model):
      ip = models.GenericIPAddressField(unique=True, null=True)
      intentos = models.IntegerField(default=1)
      timestamp = models.DateTimeField(null=True)

class ArchivosA(models.Model):
      upload = models.FileField(upload_to='Practicas/')
      usuario=models.ForeignKey(Alumnos, on_delete=models.CASCADE)

      def get_file(self):
            if self.upload:
                  return '{}{}'.format(settings.MEDIA_URL, self.upload)

class ArchivosP(models.Model):
      NombreActividad = models.CharField(max_length = 20, null=True)
      upload = models.FileField(upload_to='Ejercicios/')
      #usuario=models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True)
      def get_file(self):
            if self.upload:
                  return '{}{}'.format(settings.MEDIA_URL, self.upload)

