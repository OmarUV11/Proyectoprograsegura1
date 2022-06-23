from django.shortcuts import redirect
from modelo import models
from django.core.exceptions import ObjectDoesNotExist

def login_requerido_alumnos(vista):
        def interna(request, *args, **kwargs):
                logueado = request.session.get('logueado', False)
                nombre_usuario = request.session.get('nombre')
                try:
                    alumno = models.Alumnos.objects.get(NombreAlumno=nombre_usuario)
                except ObjectDoesNotExist: 
                       return redirect('/login')
                prueba = alumno.Tipocuenta
                alumno = "Alumno"
                if not logueado or prueba != alumno:
                        return redirect('/login')
                return vista(request, *args, **kwargs)
        return interna

def login_requerido_profesor(vista):
        def interna(request, *args, **kwargs):
                logueado = request.session.get('logueado', False)
                nombre_usuario = request.session.get('nombre')
                try:
                    profesor = models.Profesor.objects.get(NombreProfesor=nombre_usuario)
                except ObjectDoesNotExist: 
                       return redirect('/login')

                prueba = profesor.Tipocuenta
                maestro = "Maestro"
                if not logueado or prueba != maestro:
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
