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

def bfor(request):
    return render(request, "Integracion/bfor.html")
def bwhile(request):
    return render(request, "Integracion/bwhile.html")

def condicional(request):
    return render(request, "Integracion/condicional.html")

def listas(request):
    return render(request, "Integracion/listas.html")

def logicos(request):
    return render(request, "Integracion/logicos.html")

def tupla(request):
    return render(request, "Integracion/tuplas.html")

def correlacional(request):
    return render(request, "Integracion/correlacional.html")

def moda(request):
    # Creamos los datos para representar en el gráfico
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
    f.clear()
    return render(request, "Integracion/g_moda.html", {'data': uri})
   # return render(request, "Integracion/moda.html")

def promedio(request):
    x = []
    y = []
    data = getData(request)

    for d in data:
        x.append(d[0])
        y.append(d[1])

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    plt.bar(x, y, align="center", alpha=0.5)
    plt.xticks(x, y)
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    f.clear()
    return render(request, "Integracion/g_promedio.html", {'data2': uri})

def regresionlineal(request):
    dias = []
    casos = []
    data = getData(request)

    for d in data:
        dias.append(d[0])
        casos.append(d[1])

    # Creamos una figura y le dibujamos el gráfico
    f = plt.figure()
    # Creamos los ejes
    plt.pie(casos, labels=dias, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis("equal")
    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    f.clear()
    return render(request, "Integracion/g_regresionlineal.html", {'data3': uri})


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
    f.clear()
    return render(request, "Integracion/g_moda.html", {'data': uri})

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