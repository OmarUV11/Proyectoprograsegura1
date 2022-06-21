from django.shortcuts import redirect
from modelo import models

def login_requerido_prueba(vista):
        def interna(request, *args, **kwargs):
                logueado = request.session.get('logueado', False)
                nombre_usuario = request.session.get('nombre')
                alumno = models.Alumnos.objects.get(NombreAlumno=nombre_usuario)
                prueba = alumno.Tipocuenta
                Alumno = "Alumno"
                if not logueado or prueba != Alumno:
                        return redirect('/login')
                return vista(request, *args, **kwargs)
        return interna



def login_requerido(vista):
        def interna(request, *args, **kwargs):
                logueado = request.session.get('logueado', False)
                if not logueado:
                        return redirect('/login')
                return vista(request, *args, **kwargs)
        return interna

def login_requerido2(vista):
        def interna(request, *args, **kwargs):
                logueado = request.session.get('logueado2', False)
                if not logueado:
                        return redirect('/login')
                return vista(request, *args, **kwargs)
        return interna
