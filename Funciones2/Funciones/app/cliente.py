import socket
import threading
import sys

import mensajes

def conectar_servidor(host, puerto):
    # socket para IP v4
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((host, int(puerto)))
        return cliente
    except:
        print('Servidor inalcanzable')
        exit()

def leer_mensajes(cliente):
    while True:
        mensaje = mensajes.leer_mensaje(cliente)
        print('-->' + mensaje.decode('utf-8'))


def enviar_mensaje_loop(cliente):
    mensaje = b''
    while mensaje.strip() != b'exit':
        mensaje = input('Mensaje: ')
        mensaje = mensaje.encode('utf-8')
        mensajes.mandar_mensaje(cliente, mensaje)     

      
if __name__ == '__main__':
    host = '0.0.0.0'
    puerto = 8002
    cliente = conectar_servidor(host, puerto)
    hilo = threading.Thread(target=leer_mensajes, args=(cliente,))
    hilo.start()
    enviar_mensaje_loop(cliente)
