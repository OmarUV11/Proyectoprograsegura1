from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.conf import settings
import subprocess


def verificar_scripts(request):
  t = 'SubirEjercicios.html'
  Entrada = request.POST.get('Entrada','')
<<<<<<< HEAD
  Salida_esperada =  request.POST.get('Salida_esperada','')
  Comando = ['/home/omarconde/hola.sh',Entrada]
  salida = subprocess.Popen(Comando,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = salida.communicate()
  print(stdout, stderr)
  if Salida_esperada == stdout.decode('utf-8').strip():
     print("Ejercicio Correcto")
  else:
     print("Ejercicio Incorrecto")
=======
  Comando = ['/home/omarconde/hola.sh',Entrada]
  salida_esperada = 'hola %Entrada'
  salida = subprocess.Popen(Comando,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = salida.communicate()
  print(stdout, stderr)
  salida_esperada == stdout.decode('utf-8').strip()
>>>>>>> f383b1942dabeb0c7c70fa3ed0e31a9077ed13b6
  return render(request,t)

def password_valido(password, pass_hasheado, salt):
   binario = (password + salt).encode('utf-8')
   hasher = hashlib.sha256()
   hasher.update(binario)
   return hasher.hexdigest() == pass_hasheado

