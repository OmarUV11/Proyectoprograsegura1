from django.db import models

# Create your models here.
class Usuario(models.Model):
      nombre = models.CharField(max_length = 25)
      contraseña = models.CharField(max_length = 100)

class Alumnos(models.Model):
      NombreAlumno = models.CharField(max_length = 60)
      Matricula =  models.CharField(max_length = 60)
      Contraseña = models.CharField(max_length = 100)
      Tipocuenta = models.CharField(max_length = 60, null=True)
      Chat_id = models.CharField(max_length = 60, null=True)
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
            return '{}{}'.format(settings.MEDIA_URL, self.upload)

class Practicas(models.Model):
      NombrePractica = models.CharField(max_length=50)
      Descripcion = models.TextField(max_length=200)
      Entrada = models.CharField(max_length=30)
      Esperada = models.CharField(max_length=30)
      Archivo = models.FileField(upload_to='Practicas_Maestro/')

      def __str__(self):
            return self.NombrePractica

      def get_absolute_url(self):
            return reverse('detalle-practica', args=[str(self.id)])