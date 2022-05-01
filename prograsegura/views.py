from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.conf import settings
import subprocess


def verificar_scripts(request):
  t = 'SubirEjercicios.html'
  Entrada = request.POST.get('Entrada','')
  Comando = ['/home/omarconde/hola.sh',Entrada]
  salida_esperada = 'hola %Entrada'
  salida = subprocess.Popen(Comando,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = salida.communicate()
  print(stdout, stderr)
  salida_esperada == stdout.decode('utf-8').strip()
  return render(request,t)

