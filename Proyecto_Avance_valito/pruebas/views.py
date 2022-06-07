from django.http import HttpResponse, JsonResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.conf import settings
from modelo import models
from django.utils.crypto import get_random_string
from datetime import timezone
import logging, platform
import pruebas.settings as conf
import datetime
import subprocess
import requests
import string
import random
import re
import hashlib
import os, sys, stat

def crear_actividad(request):
    t = 'Crear_ejercicio.html'
    titulo = request.POST.get('Titulo','')
    descripcion = request.POST.get('Descripcion','')
    entrada = request.POST.get('entrada', '')
    esperada = request.POST.get('esperada','')
    archivo = request.FILES.get('archivosubido')

    practica = models.Practicas(NombrePractica=titulo,Descripcion=descripcion,Entrada=entrada, Esperada=esperada, Archivo=archivo)

    practica.save()

    return render(request, t)


def comparar_script(entradaScript, esperadaScript, archivo):
    entrada = entradaScript
    esperada = esperadaScript

    comando = [archivo, entrada]
    salida = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = salida.communicate()

    if esperada == stdout.decode('utf-8').strip():
        return True
    else:
        return False


def SubirEjerciciosProfesor(request):
  t = 'SubirEjerciciosProfesor.html'
  file = request.FILES.get('archivosubido')
  NombreArchivo = request.POST.get('Nombre_Archivo','')
  archivo = models.ArchivosP(upload=file, NombreActividad=NombreArchivo)
  
  archivo.save()
  tarea = models.ArchivosP.objects.all()

  return render(request,t, {'tarea':tarea})


def verificar_scripts(request):
  t = 'SubirEjercicios.html'

  entrada = request.POST.get('Entrada','')
  esperada =  request.POST.get('Salida_esperada','')
  file = request.FILES.get('archivosubido')
  NombreUsuario = request.session.get('nombre')
  ObtenerAlumno = models.Alumnos.objects.get(NombreAlumno=NombreUsuario)
  print(ObtenerAlumno.id)

#--
  TareaProfe = models.ArchivosP.objects.all()
  #hola = TareaProfe.pk
  #print(hola)
#--
#  alumnosScript=models.Alumnos.objects.get(pk=8)
  archivo = models.ArchivosA(upload=file, usuario=ObtenerAlumno)
  archivo.save()

  obj = models.ArchivosA.objects.get(upload=archivo.upload, usuario_id=ObtenerAlumno)
  print(obj.upload.path)
  ruta = obj.upload.path
  os.chmod(ruta, stat.S_IXUSR)
  comando = [ruta, entrada]
  salida = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = salida.communicate()
  print(stdout,stderr)

  if esperada == stdout.decode('utf-8').strip():
     print("Ejercicio Correcto")
  else:
     print("Ejercicio Incorrecto")
  return render(request,t,{'TareaProfe':TareaProfe})



def mandar_mensaje_al_bot(request):
    print("Entro la funcion =)")
    nombre = request.session.get('nombre','anonimo')
    datos_guardados = models.Alumnos.objects.get(NombreAlumno=nombre)
    Chat_id = datos_guardados.Chat_id
    token = datos_guardados.Token_tel
    mensaje_bot = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + Chat_id + '&parse_mode=Markdown&text='+ mensaje_bot
    requests.get(send_text)
    models.Alumnos()
    models.Alumnos.objects.filter(NombreAlumno=nombre).update(Token_Env=mensaje_bot, Token_Tem=datetime.datetime.now())
    

def disminuir_tiempo_actual_yalmaceno(tiempo_almacenado):
    print("Entro a esta funcion del tiempo")
    tiempo_actual = datetime.datetime.now(timezone.utc)
    diferencia = tiempo_actual - tiempo_almacenado
    return diferencia.seconds    


def verificar_token(request):
    t = 'Verficiacion_token.html'
    nombre = request.session.get('nombre','anonimo')
    if request.method == 'GET':
        return render(request, t)
    elif request.method == 'POST':
        ip_cliente = get_client_ip(request)
        if puede_hacer_peticion(ip_cliente):
           token = request.POST.get('Token','').strip()
           print(token)
           try:
               token_almacenado = models.Alumnos.objects.get(Token_Env=token)
               if (disminuir_tiempo_actual_yalmaceno(token_almacenado.Token_Tem) > 160):  
                    errores={'El token ha expirado'}
                    return render(request,t,{'errores':errores})
               request.session['logueado2'] = True
               request.session['nombre'] = nombre
               logging.info("usuario logueado:" + nombre)
               return redirect('/verificar_scripts')
           except:
               errores = ['token incorrecto']
               return render(request, "login.html", {'errores': errores})
        else:
           return HttpResponse("Agotaste tus intentos espera 1 minuto") 

def login(request):
    if request.method == 'GET':
       t = 'login.html'
       return render(request,t)
    elif request.method == 'POST':
        nombre = request.POST.get('nombres','')
        contraseña =  request.POST.get('password','')
        if puede_hacer_peticion(get_client_ip(request)): 
              try:
                  alumno = models.Alumnos.objects.get(NombreAlumno=nombre)
                  if password_valido(contraseña, alumno.Contraseña, alumno.salt):
                     request.session['logueado']= True
                     request.session['nombre'] = nombre
                     #mandar_mensaje_al_bot(request)
                     #return redirect('/verificar_token')
                     return redirect('/verificar_scripts')
              except:
                     errores = ['crendeicales o nombre incorrectas']
                     return render(request,'login.html',{'errores',errores})
        else:
             return HttpResponse("Agotaste todos los intentos prueba intente en un minuto") 

def password_valido(password, pass_hasheado, salt):
   binario = (password + salt).encode('utf-8')
   hasher = hashlib.sha256()
   hasher.update(binario)
   return hasher.hexdigest() == pass_hasheado

def Registro_Alumnos(request):
    t = 'Registro_Alumnos.html';
    if request.method == 'GET':
       return render(request,t,{})
    elif request.method == 'POST':
       nombre = request.POST.get('nombreAlumno','').strip()
       matricula = request.POST.get('Matricula','').strip()
       contrasena =  request.POST.get('Contrasena','').strip()
       Tipocuenta = request.POST.get('TipoCuenta','').strip()
       chat_id = request.POST.get('Chat_id','').strip()
       token_telegram = request.POST.get('token_tel','').strip()
       if Tipocuenta == "Alumno":
          alumno =  models.Alumnos(NombreAlumno=nombre, Matricula=matricula, Contraseña=contrasena, Tipocuenta=Tipocuenta, Chat_id=chat_id, Token_tel=token_telegram)
          errores = recoleccion_de_errores_del_registro(alumno)
       elif Tipocuenta == "Maestro":
          profesor =  models.Profesor(NombreProfesor=nombre, Matricula=matricula, Contraseña=contrasena, Tipocuenta=Tipocuenta, Chat_id=chat_id, Token_tel=token_telegram)
          errores = recoleccion_de_errores_del_registro_profesor(profesor)
       if not errores:
          Elsalt = get_random_string(length=16)
          binario = (contrasena + Elsalt).encode('utf-8')
          hasher = hashlib.sha256()
          hasher.update(binario)
          alumno = models.Alumnos(NombreAlumno=nombre, Matricula=matricula, Contraseña=hasher.hexdigest(), Tipocuenta=Tipocuenta, Chat_id=chat_id, Token_tel=token_telegram, salt=Elsalt)
          profesor = models.Profesor(NombreProfesor=nombre, Matricula=matricula, Contraseña=hasher.hexdigest(), Tipocuenta=Tipocuenta, Chat_id=chat_id, Token_tel=token_telegram, salt=Elsalt)
          if Tipocuenta == "Alumno":
             alumno.save()
             return redirect('/login')
          else:
             profesor.save()
             return redirect('/login')
       else:
          contexto = {'errores':errores}
          return render(request,t,contexto)

def verificacion_de_contrasenas(alumno):
    caracteres_especiales = "[@_!#$%^&*()<>?/|}{~:]";
    errores_contrasena = []
    if ' ' in alumno.Contraseña:
            errores_contrasena.append('La contraseña no debe contener espacios')
    if len(alumno.Contraseña) < 10:
               errores_contrasena.append('La contraseña debe contener al menos 10 caracteres')
    if not any(caracter.isupper() for caracter in alumno.Contraseña):
               errores_contrasena.append('La contraseña al menos debe contener una letra mayúscula')
    if not any(caracter.islower() for caracter in alumno.Contraseña):
               errores_contrasena.append('La contraseña debe de contar con al menos una letra minuscula')
    if not any(caracter.isdigit() for caracter in alumno.Contraseña):
               errores_contrasena.append('La contraseña debe de contar con al menos con un numero')
    return errores_contrasena

def verificacion_de_contrasenas_profesor(profesor):
    caracteres_especiales = "[@_!#$%^&*()<>?/|}{~:]";
    errores_contrasena = []
    if ' ' in profesor.Contraseña:
            errores_contrasena.append('La contraseña no debe contener espacios')
    if len(profesor.Contraseña) < 10:
               errores_contrasena.append('La contraseña debe contener al menos 10 caracteres')
    if not any(caracter.isupper() for caracter in profesor.Contraseña):
               errores_contrasena.append('La contraseña al menos debe contener una letra mayúscula')
    if not any(caracter.islower() for caracter in profesor.Contraseña):
               errores_contrasena.append('La contraseña debe de contar con al menos una letra minuscula')
    if not any(caracter.isdigit() for caracter in profesor.Contraseña):
               errores_contrasena.append('La contraseña debe de contar con al menos con un numero')
    return errores_contrasena

def recoleccion_de_errores_del_registro(alumno):
    errores = []
    if alumno.NombreAlumno == '':
              errores.append('El nombre del usuario esta vacio')
    if alumno.Matricula == '':
              errores.append('La matricula esta vacia')
    if alumno.Contraseña == '':
              errores.append('La contraseña esta vacia')
    if alumno.Tipocuenta == '':
              errores.append('EL tipo de cuenta esta vacio')
    if alumno.Chat_id == '':
              errores.append('El chat_id del registro esta vacio')
    if alumno.Token_tel == '':
              errores.append('El token del registro esta vacio')
    
    errores_contrasena = verificacion_de_contrasenas(alumno)
    errores += errores_contrasena
    return errores

def recoleccion_de_errores_del_registro_profesor(profesor):
    errores = []
    if profesor.NombreProfesor == '':
              errores.append('El nombre del usuario esta vacio')
    if profesor.Matricula == '':
              errores.append('La matricula esta vacia')
    if profesor.Contraseña == '':
              errores.append('La contraseña esta vacia')
    if profesor.Tipocuenta == '':
              errores.append('EL tipo de cuenta esta vacio')
    if profesor.Chat_id == '':
              errores.append('El chat_id del registro esta vacio')
    if profesor.Token_tel == '':
              errores.append('El token del registro esta vacio')
    
    errores_contrasena = verificacion_de_contrasenas_profesor(profesor)
    errores += errores_contrasena
    return errores


def get_client_ip(request):
    print("Entro a la funcion para obtener la ip del usurio")
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def es_ip_conocida(ip: str):
    registros = models.IntentosIP.objects.filter(ip=ip)
    return len(registros) != 0


def guardar_peticion(ip: str, intentos: int):
    fecha_actual = datetime.datetime.now()
    if not es_ip_conocida(ip):
        entrada = models.IntentosIP(ip=ip, intentos=1,timestamp=fecha_actual)
        entrada.save()
        return
    registro = models.IntentosIP.objects.get(ip=ip)
    registro.intentos = intentos
    registro.timestamp = fecha_actual
    registro.save()
   
def esta_tiempo_en_ventana(timestamp):
    momento_actual = datetime.datetime.now(timezone.utc)
    resta = momento_actual - timestamp
    if resta.seconds < conf.VENTANA_SEGUNDOS_INTENTOS_PETICION:
        return True
    return False

def puede_hacer_peticion(ip):
    """
    Verdadero si la IP no ha alcanzado el límite de intentos.

    Keyword Arguments:
    ip --
    returns: Bool
    """
    if not es_ip_conocida(ip):
        guardar_peticion(ip, 1)
        return True
    registro = models.IntentosIP.objects.get(ip=ip)
    if not esta_tiempo_en_ventana(registro.timestamp):
        guardar_peticion(ip, 1)
        return True
    else:
        if (registro.intentos + 1) > conf.INTENTOS_MAXIMOS_PETICION:
            guardar_peticion(ip, registro.intentos + 1)
            return False
        else:
            guardar_peticion(ip, registro.intentos + 1)
            return True

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO,
                    filename='resgistros.log', filemode='a')
