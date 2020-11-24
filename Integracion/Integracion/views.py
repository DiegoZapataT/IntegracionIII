from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from random import sample
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
import io, urllib, base64
from mongoconnect.views import getData, getData1, listar_colecciones_db
import json
import os

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
    x = []
    y = []
    data = getData1(request)

    for d in data:
        x.append(d[0])
        y.append(d[1])
    f = plt.figure()
    dict_data = {'var1':x,'var2':y}
    df = pd.DataFrame(dict_data)
    corr_matrix = df.corr()
    ff, ax = plt.subplots(figsize=(9, 8))
    sns.heatmap(corr_matrix, ax=ax, cmap="YlGnBu", linewidths=0.1, annot=True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    f.clear()
    return render(request, "Integracion/correlacional.html", {'data': uri})


def users(request):
    return render(request, "Integracion/users.html")

def charts(request):
    return render(request, "Integracion/charts.html")

def moda(request):
    # Creamos los datos para representar en el gráfico
    x = []
    y = []
    data = getData1(request)
    
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

# def promedio(request):
#     x = []
#     y = []
#     data = getData(request)

#     for d in data:
#         x.append(d[0])
#         y.append(d[1])

#     # Creamos una figura y le dibujamos el gráfico
#     f = plt.figure()
#     plt.bar(x, y, align="center", alpha=0.5)
#     plt.xticks(x, y)
#     # Como enviaremos la imagen en bytes la guardaremos en un buffer
#     buf = io.BytesIO()
#     plt.savefig(buf, format='png')
#     buf.seek(0)
#     string = base64.b64encode(buf.read())
#     uri = urllib.parse.quote(string)
#     f.clear()
#     return render(request, "Integracion/g_promedio.html", {'data2': uri})

def promedio(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = open(os.path.join(settings.MEDIA_ROOT, myfile.name), 'rb').read()
        data = str(data,'utf-8')
        data = json.loads(data)
        lenData = len(data)
        pKeys = []
        sKeys = []
        j = 0
        for i in range(0, lenData):
            keys1 = []
            for k in data[i].keys():
                keys2 = []
                keys1.append(k)
                # try: #data[i][k][j].keys():
                #     for ke in data[i][k][j].keys():
                #         keys2.append(ke)
                # except: a = "pos nada"
                # pKeys[i][k].append(keys2)
                # j += 1

            pKeys.append(keys1)

        data3 = data[0][pKeys[0][2]]
        return render(request, "Integracion/g_promedio.html", {
            'uploaded_file_url': lenData, 'data2': data3, 'data3': pKeys
        })
    no = "nope"
    return render(request, "Integracion/g_promedio.html", {
            'uploaded_file_url': no
        })

def dataPromedio(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            yes="yes"
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def regresionlineal(request):
    dias = []
    casos = []
    data = getData1(request)

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

def ver_datos(request):

    lista = listar_colecciones_db(request)
    print("ver_datos recibe m= ", lista)
    return render(request, "Integracion/lista_datos.html",{'lista': lista})