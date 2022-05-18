from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.conf import settings
import subprocess


def verificar_scripts(request):
  t = 'SubirEjercicios.html'
  Entrada = request.POST.get('Entrada','')
  Salida_esperada =  request.POST.get('Salida_esperada','')
  Archivo = request.POST.get('Archivos')
  print(Archivo)
  Comando = ['/home/omarconde/hola.sh',Entrada]
  salida = subprocess.Popen(Comando,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = salida.communicate()
  print(stdout, stderr)
  if Salida_esperada == stdout.decode('utf-8').strip():
     print("Ejercicio Correcto")
  else:
     print("Ejercicio Incorrecto")
  return render(request,t)




def login(request):
    t = 'login.html'
    logueado = request.session.get('logueado', False)
    if request.method == 'GET':
       return render(request,t,{'logueado': logueado})
    if request.method == 'POST':
         nombre = request.POST.get('nombres','')
         contraseña =  request.POST.get('password','')
         try:
             admin = models.administrador.objects.get(nombre=nombre)
             if password_valido(contraseña, admin.contraseña, admin.salt):
                request.session['logueado']= True
                request.session['nombre']= nombre
                return redirect('/verificar_scripts')
         except:
                return redirect('/login')

def Registro_Alumnos(request):
    t = 'Registro_Usuarios'
    if request.method == 'GET':
       return render(request,t,{})
    elif request.method == 'POST':
       nombre = request.POST.get('nombreAlumno','')
       matricula = request.POST.get('Matricula','')
       contrasena =  request.POST.get('Contrasena','').strip()
       alumno =  models.Alumnos(NombreAlumno=nombre,Matricula=matricula,contrasena=Contraseña)
       alumno.save()
       return redirect('/login')
