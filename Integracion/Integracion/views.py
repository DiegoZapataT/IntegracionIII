from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from random import sample
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
import io, urllib, base64
from mongoconnect.views import getData

def index(request):
    return render(request, "Integracion/index.html")

def tutorial(request):
    return render(request, "Integracion/tutorial.html")

def moda(request):
    # Creamos los datos para representar en el gráfico
    ##plt.plot(range(11))
    ##f = plt.gcf()
    plt.clf()
    x = []
    y = []
    data = getData(request)
    
    for d in data:
        x.append(d[0])
        y.append(d[1])

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()

    # Creamos los ejes
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes.plot(x, y)
    axes.set_xlabel("Eje X")
    axes.set_ylabel("Eje Y")
    
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    f.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "Integracion/moda.html", {'data': uri})
   # return render(request, "Integracion/moda.html")

def promedio(request):
    plt.clf()
    x = []
    y = []
    data = getData(request)
    
    for d in data:
        x.append(d[0])
        y.append(d[1])

    # Creamos una figura y le dibujamos el gráfico
    plt.bar(x,y, align="center",alpha=0.5)
    plt.xticks(x,y)
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "Integracion/promedio.html", {'data2': uri})

def regresionlineal(request):
    plt.clf()
    dias = []
    casos = []
    data = getData(request)
    
    for d in data:
        dias.append(d[0])
        casos.append(d[1])

    # Creamos una figura y le dibujamos el gráfico
    # Creamos los ejes
    plt.pie(casos, labels=dias, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis("equal")
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "Integracion/regresionlineal.html", {'data3': uri})
   
def faq(request):
    return render(request, "Integracion/faq.html")

