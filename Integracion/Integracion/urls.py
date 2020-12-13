"""Integracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Integracion.views import index, tutorial, charts, users, moda, faq, bfor, listas, tupla, logicos, condicional, bwhile, ver_datos, ver_datos2, PCregreCSV, PCverARQUE, promedio, graficov2, buscador_paciente
from mongoconnect import views
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('subir_archivo/', promedio),
    path('PCverARQUE/', PCverARQUE),
    path('PCregreCSV/', PCregreCSV),
    path('admin', admin.site.urls),
    path('tutorial/', tutorial),
    path('datos/', ver_datos),
    path('datos/<str:nc>/', ver_datos2),
    path('bfor/', bfor),
    path('listas/', listas),
    path('tuplas/', tupla),
    path('logicos/', logicos),
    path('condicional/', condicional),
    path('bwhile/', bwhile),
    path('moda/', moda),
    path('moda/<str:paciente>/', buscador_paciente),
    path('graficador/',graficov2),
    path('faq/', faq),
    path('users/', users),
    path('charts/', charts),
    path('', index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)