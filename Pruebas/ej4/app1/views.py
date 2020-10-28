from django.shortcuts import render
from django.http import  HttpResponse
from .formu import Valorform

def home(request):
    return render(request, 'index.html')

def form(request):
    formulario = Valorform()
    return render(request, 'formu.html', {"form": formulario})


# Create your views here.

