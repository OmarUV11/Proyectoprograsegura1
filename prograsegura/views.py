from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.conf import settings
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

