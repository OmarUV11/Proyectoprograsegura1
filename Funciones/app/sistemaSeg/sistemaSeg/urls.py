"""sistemaSeg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistemaSeg.views import *
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='login', permanent=True)),
    path('verificar_scripts',verificar_scripts),
    path('login',login),
    path('Registro_Alumnos',Registro_Alumnos),
    path('verificar_token',verificar_token),
    path('logout',logout),
    path('crear_actividad', crear_actividad),
    path('verificar_token_maestro',verificar_token_maestro),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
