"""
Servidor.

Servidor de un chat. Es una implementación incompleta:
- Falta manejo de exclusión mutua
- Falta poder desconectar de forma limpia clientes
- Falta poder identificar clientes
"""


import socket
import threading
import sys
import os, stat
import mensajes
import subprocess
import shutil

def enviar_mensaje_loop(cliente, resultado2):
    mensaje = resultado2
    mensaje = mensaje.encode('utf-8')
    mensajes.mandar_mensaje(cliente, mensaje)  

def comparar_script(entradaScript, esperadaScript, archivo):
    #os.chmod(archivo, 0o755)
    comando = [archivo, entradaScript]
    salida = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = salida.communicate()
    correcto='correcto'
    incorrecto='incorrecto'
    if esperadaScript == stdout.decode('utf-8').strip():
       return correcto
    else:
        return incorrecto

def crear_socket_servidor(puerto):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('', int(puerto)))  # hace el bind en cualquier interfaz disponible
    return servidor


def broadcast(mensaje, clientes):
    for cliente in clientes:
        mensajes.mandar_mensaje(cliente, mensaje)

        
# Hilo para leer mensajes de clientes
def atencion(cliente, clientes):
  #  while True:
        mensaje = mensajes.leer_mensaje(cliente)
        msj = mensaje.decode('utf-8').strip()
        print(msj)
        lista = msj.split('|')
        print(lista[0])
        print(lista[1])
        print(lista[2])
        #shutil.chown(lista[0], user='root',group='root')
        if mensaje.strip() != b'exit':
           resultado = comparar_script(lista[1], lista[2], lista[0])
           print(resultado)
           #resultado2 = resultado.encode('utf-8')
           enviar_mensaje_loop(cliente, resultado)

           #mensajes.mandar_mensaje(cliente, resultado2)
           cliente.close()
           return
        #broadcast(resultado2, clientes)
    

def escuchar(servidor):
    servidor.listen(5) # peticiones de conexion simultaneas
    clientes = []
    while True:
        cliente, _ = servidor.accept() # bloqueante, hasta que llegue una peticion
        clientes.append(cliente)
        hiloAtencion = threading.Thread(target=atencion, args=(cliente, clientes)) # se crea un hilo de atención por cliente
        hiloAtencion.start()



if __name__ == '__main__':
    
    servidor = crear_socket_servidor(8002)
    print('Escuchando...')
    escuchar(servidor)
