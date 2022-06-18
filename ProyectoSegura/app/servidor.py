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

import mensajes


def crear_socket_servidor(puerto):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('', int(puerto)))  # hace el bind en cualquier interfaz disponible
    return servidor


def broadcast(mensaje, clientes):
    for cliente in clientes:
        mensajes.mandar_mensaje(cliente, mensaje)


def atencion(cliente, clientes):
    while True:
        mensaje = mensajes.leer_mensaje(cliente)
        if mensaje.strip() == b'exit':
            cliente.close()
            return
        broadcast(mensaje, clientes)
    

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
