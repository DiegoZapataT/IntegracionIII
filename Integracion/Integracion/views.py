from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def index(request):
    return render(request, "Integracion/index.html")

def tutorial(request):

    return render(request, "Integracion/tutorial.html")

def moda(request):

   return render(request, "Integracion/moda.html")

def promedio(request):

    return render(request, "Integracion/promedio.html")

def regresionlineal(request):
    
    return render(request, "Integracion/regresionlineal.html")

def faq(request):
    return render(request, "Integracion/faq.html")