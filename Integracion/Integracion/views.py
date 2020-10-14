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
    x = []
    y = []
    data = getData(request)
    
    x = range(1,11)
    y = sample(range(20), len(x))

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
    return render(request, "Integracion/moda.html", {'data': data})
   # return render(request, "Integracion/moda.html")

def promedio(request):

    return render(request, "Integracion/promedio.html")

def regresionlineal(request):
    
    return render(request, "Integracion/regresionlineal.html")

def faq(request):
    return render(request, "Integracion/faq.html")

def plot(request):
    # Creamos los datos para representar en el gráfico
    x = range(1,11)
    f = plt.gcf()
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    f.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, "Integracion/moda.html", {'data': uri})

    # canvas = FigureCanvasAgg(f)
    # canvas.print_png(buf)

    # # Creamos la respuesta enviando los bytes en tipo imagen png
    # response = HttpResponse(buf.getvalue(), content_type='image/png')

    # # Limpiamos la figura para liberar memoria
    # f.clear()

    # # Añadimos la cabecera de longitud de fichero para más estabilidad
    # response['Content-Length'] = str(len(response.content))

    # # Devolvemos la response
    # return response