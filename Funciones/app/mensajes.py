"""
mensajes.

Módulo utileria para manejo de mensajes de chat
"""


DELIMITADOR = b'\r\n'


def quitar_delimitador(mensaje):
    """
    Limpia un mensaje para que no tenga delemitador.

    Keyword Arguments:
    mensaje -- 
    returns: bytes
    """
    if not mensaje.endswith(DELIMITADOR):
        return mensaje
    return mensaje[:-len(DELIMITADOR)]


def leer_mensaje(socket):
    """
    Permite leer un mensaje de longitud arbitraria, utilizando delimitadores de mensaje.

    Keyword Arguments:
    socket de cliente
    returns: bytes
    """
    chunk = socket.recv(1024)
    mensaje = b''
    while not chunk.endswith(DELIMITADOR):
        mensaje += chunk
        chunk = socket.recv(1024)
    mensaje += chunk
    return quitar_delimitador(mensaje)


def mandar_mensaje(socket, mensaje):
    """
    Manda un mensaje tomando en cuenta el delimitador.

    Keyword Arguments:
    socket es el socket de servidor o cliente destino
    mensaje bytes de mensaje 
    returns: None
    """
    socket.send(mensaje + DELIMITADOR)
