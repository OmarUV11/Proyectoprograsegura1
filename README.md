# -Proyecto Escolar Universidad Veracruzana 
# Orquestación de Infraestructura Segura mediante Microservicios y Bash

Este repositorio aloja una solución automatizada y robusta de infraestructura cliente-servidor construida bajo una arquitectura de microservicios. El proyecto implementa un entorno altamente seguro, aislando los componentes mediante contenedores Docker, gestionando el tráfico web a través de un proxy inverso y aplicando políticas estrictas de seguridad (hardening) a nivel de sistema operativo y sockets.

## 🏗️ Arquitectura del Sistema

La solución está completamente orquestada a través de `docker-compose.yml` e interactúa mediante tres capas aisladas dentro de una red interna de contenedores:

1. **Proxy Inverso (Nginx):** Actúa como la puerta de entrada única del sistema operativo host, exponiendo los puertos estándar `80` (HTTP) y `443` (HTTPS). Gestiona certificados de seguridad SSL, archivos estáticos y redirige las peticiones internas de forma segura hacia el contenedor de la aplicación.
2. **Servidor de Aplicaciones (App):** Basado en una imagen personalizada de `Python 3.9` (`Dockerfile`). Ejecuta la lógica del backend mediante un servidor WSGI de producción (Gunicorn) y aloja scripts sockets concurrentes multihilo para la comunicación y evaluación controlada de scripts.
3. **Persistencia de Datos (MariaDB):** Base de datos relacional aislada que almacena la información del sistema de manera persistente a través de volúmenes mapeados en el sistema de archivos local (`./data`).

## 🛡️ Características de Seguridad e Ingeniería Implementadas

* **Hardening en Dockerfile (Principio de Privilegios Mínimos):** La imagen de la aplicación rompe el esquema por defecto de ejecución como usuario `root`. Se crean usuarios del sistema dedicados (`usuario1` y `usuario2`) y se restringen los permisos de los directorios críticos mediante políticas estrictas de Linux (`chmod 500` / `chown`) para prevenir ataques de escalada de privilegios o ejecuciones maliciosas en caliente.
* **Inyección Dinámica de Secretos:** Los datos de conexión y llaves criptográficas no se encuentran expuestos en el código fuente. El inicio del entorno es controlado por un script automatizador en Bash (`levantar_sistema.sh`) que descifra al vuelo los archivos de configuración (`app.env` y `bd.env`) mediante herramientas CLI y exporta las variables de entorno necesarias para aprovisionar el stack de Docker de forma transparente.
* **Manejo Concurrente de Sockets:** Los componentes `servidor.py` y `cliente.py` establecen canales de comunicación TCP de baja latencia utilizando hilos (`threading`) para manejar flujos paralelos de atención, implementando mecanismos limpios de delimitación de tramas de bytes y ejecución de subprocesos controlados (`subprocess`).

## 🚀 Guía de Despliegue Rápido

### Requisitos Previos
* Motor de Docker (Docker Engine) v20.10+
* Docker Compose v2.0+
* Sistema Operativo basado en Linux (Debian/Ubuntu preferentemente)

### Pasos para Inicializar la Infraestructura

1. Clonar el repositorio en su servidor local:
```bash
git clone [https://github.com/OmarUV11/ProyectoFinal.git](https://github.com/OmarUV11/ProyectoFinal.git)
cd ProyectoFinal
