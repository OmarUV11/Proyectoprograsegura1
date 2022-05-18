from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.conf import settings
from modelo import models
import subprocess

def verificar_scripts(request):
  t = 'SubirEjercicios.html'
  Entrada = request.POST.get('Entrada','')
  Salida_esperada =  request.POST.get('Salida_esperada','')
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
         IP = ip = get_client_ip(request)
         print(IP)
         nombre = request.POST.get('nombres','')
         contraseña =  request.POST.get('password','')
   
         try:
             admin = models.Usuario.objects.get(nombre=nombre,contraseña=contraseña,)
             #if password_valido(contraseña, admin.contraseña):
             request.session['logueado']= True
             request.session['nombre']= nombre
             return redirect('/verificar_scripts')
         except:
                return redirect('/login')


def Registro_Alumnos(request):
    t = 'Registro_Alumnos.html';
    if request.method == 'GET':
       return render(request,t,{})
    elif request.method == 'POST':
       nombre = request.POST.get('nombreAlumno','')
       matricula = request.POST.get('Matricula','')
       contrasena =  request.POST.get('Contrasena','').strip()
       Tipocuenta = request.POST.get('TipoCuenta','')
       alumno =  models.Alumnos(NombreAlumno=nombre,Matricula=matricula,Contraseña=contrasena,Tipocuenta=Tipocuenta)
       alumno.save()
       return redirect('/login')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
