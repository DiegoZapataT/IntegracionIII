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
from Integracion.views import index, tutorial, charts, users, moda, promedio, regresionlineal, faq, correlacional,listas, tupla, logicos, condicional, bwhile, bfor
from mongoconnect import views
 
urlpatterns = [
    path('admin', admin.site.urls),
    path('tutorial/', tutorial),
    path('bfor/', bfor),
    path('listas/', listas),
    path('tuplas/', tupla),
    path('logicos/', logicos),
    path('condicional/', condicional),
    path('bwhile/', bwhile),
    path('moda/', moda),
    path('promedio/', promedio),
    path('correlacional/', correlacional),
    path('regresionlineal/', regresionlineal),
    path('faq/', faq),
    path('users/', users),
    path('charts/', charts),
    path('', index),
    path('add_post/', views.add_post),
    path('update_post/<int:id>',views.update_post),
    path('delete_post/<int:id>', views.delete_post),
    path('getData', views.getData),
    path('read_post/<str:id>', views.read_post),
    path('read_post_all', views.read_post_all, name='realdall'),
]
