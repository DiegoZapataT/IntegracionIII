from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.shortcuts import redirect
from random import sample
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from sklearn.linear_model import LinearRegression
import numpy as np
import io, urllib, base64
from mongoconnect.views import getData, getData1, listar_colecciones_db, listar_datos_col, lista_indices
import json
import os
import Integracion.grafico as grafico
import Integracion.grafico2 as grafico2
import Integracion.paciente_stats as paciente_stats
from bson.json_util import dumps


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


#Avance de paulina, crear grafico regresion lineal con datos leidos dede un csv
def PCregreCSV(request):
    datos = pd.read_csv('datos.csv')
    datos.head()
    fig   = plt.figure(figsize=(14,14))
    plt.scatter(datos['y'],datos['x'])
    plt.plot(datos['y'],datos['x'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    datos.keys()

    ny = datos['y'].values.reshape(-1,1)
    nx = datos['x'].values.reshape(-1,1)
    lg = LinearRegression()
    lg.fit(ny, nx)
    xp = lg.predict(ny)

    m = lg.coef_[0][0]
    c = lg.intercept_[0]

    fig = plt.figure(figsize=(25,14))
    plt.plot(datos['y'],datos['x'],label='a')
    plt.plot(ny, xp, color='red', label='b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'Integracion/PCregreCSV.html',{'data':uri})

#Avance de paulina, crear grafico regresion lineal con datos numericos digitados por teclado
def PCregreINP(request):
    n = 50
    x = request.POST.getlist('x')
    y = request.POST.getlist('y')

    # si ya se hizo submit de formulario...
    if(x):
        # convierte las listas x, y en diccionario
        # pero solo con filas que tengan contenido
        data  = [["x","y"]]
        for i in range(len(x)):
            if x[i] != '':
                data.append([float(x[i]),float(y[i])])

        # quita los encabezado de columna
        cols  = data.pop(0)

        # crea el data frame con los datos
        datos = pd.DataFrame(data, columns=cols)
        datos.keys()
        ny = datos['y'].values.reshape(-1,1)
        nx = datos['x'].values.reshape(-1,1)
        lg = LinearRegression()
        lg.fit(ny, nx)
        xp = lg.predict(ny)
        m  = lg.coef_[0][0]
        c  = lg.intercept_[0]

        # grafica los datos y su regresion lineal
        fig = plt.figure(figsize=(25,14))
        plt.scatter(datos['y'],datos['x'])
        plt.plot(datos['y'],datos['x'])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid()

        plt.plot(ny, xp, color='red',   label='b')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()

        # prepara imagen de salida
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri =  urllib.parse.quote(string)
        return render(request,'Integracion/PCgrafico.html',{'data':uri})


    context={}
    context['veces'] = range(1,n)

    return render(request, 'Integracion/PCregreINP.html', context)

#Avance de paulina, ver datos del archivo arquetipos.json
def PCverARQUE(request):
    with open('arquetipos.json', encoding="utf-8") as json_file: 
        datos = json.load(json_file)
    return render(request, "Integracion/PCverARQUE.html",{'jdatos':datos})

def users(request):
    return render(request, "Integracion/users.html")

def charts(request):
    return render(request, "Integracion/charts.html")

def moda(request):
    Var=''
    Contador=[]
    Variable=[]
    Moda=[]
    Total=0

    if request.method == "POST":
        if request.POST['paciente_nombre']:
            paciente = request.POST['paciente_nombre']
            return redirect('/moda/' + paciente + '/')
        if request.POST['drop2']:
            Var = request.POST['drop2']
            Variable, Contador, Moda, Total = grafico.Frecuencia(Var)

    print("Contador :",Contador)
    print(Variable)

    return render(request, "Integracion/g_moda.html", {"parametros":(Var,Moda,Total),"Variable":Variable,"Contador":Contador,"Moda":Moda,"Total":Total})

def barra(request):
    Var=''
    Contador=[]
    Variable=[]
    Moda=[]
    Total=0

    if request.method == "POST":
        if request.POST['drop2']:
            Var = request.POST['drop2']
            Variable, Contador, Moda, Total = grafico.Frecuencia(Var)

    print("Contador :",Contador)
    print(Variable)

    return render(request, "Integracion/g_barra.html", {"parametros":(Var,Moda,Total),"Variable":Variable,"Contador":Contador,"Moda":Moda,"Total":Total})

def promedio(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = open(os.path.join(settings.MEDIA_ROOT, myfile.name), 'rb').read()
        data = str(data,'utf-8')
        data = json.loads(data)
        # request.session['datajson'] = data
        data, datap, lenData, pKeys = dataJson(request, data)
        return render(request, "Integracion/g_promedio.html", {
            'uploaded_file_url': data, 'datajson': data, 'lenData': lenData, 'keysjson': pKeys[0]
        })

    return render(request, "Integracion/g_promedio.html")

def dataJson(request, data):
    lenData = len(data)
    pKeys = []
    for i in range(0, lenData):
        keys1 = []
        for k in data[i].keys():
            keys1.append(k)
        
        pKeys.append(keys1)
    datap = []
    d = []
    for i in range(0, lenData):
        dd = []
        for u in range(0, len(pKeys)):
            a = pKeys[u]
            dd.append(data[i])
        d.append(dd)
    for k in pKeys[0]:
        print (k)
    if "nombre" in pKeys[0]:
        for u in range(0,lenData):
            datap.append(data[u]['nombre'])  

    return (data, d, lenData, pKeys) 

def faq(request):
    return render(request, "Integracion/faq.html")

def ver_datos(request):
    lista_c = listar_colecciones_db()
    c_data = "none"
    if request.method == 'POST':
        if request.POST["listado_colecciones"]:
            c_nombre = request.POST["listado_colecciones"]
            #return render(request, "Integracion/lista_datos_resultados.html/aas", {'c_data': c_data, 'lista_c': lista_c, 'c_nombre': c_nombre})
            return redirect('/datos/'+c_nombre+'/')
    return render(request, "Integracion/lista_datos.html",{'c_data': c_data, 'lista_c': lista_c})

def ver_datos2(request, nc):
    c_titulo = nc
    c_data = listar_datos_col(nc)
    for i in range (len(c_data)):
        c_data[i] = (c_data[i]["_id"], dumps(c_data[i], indent=4))
    paginator = Paginator(c_data, 25)  # muestra 25 por pag.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Integracion/lista_datos_resultados.html", {'c_titulo':c_titulo, 'c_data': c_data, 'page_obj': page_obj})


def graficov2(request):
    Contador=[]
    Variable=[]
    Moda=[]
    Total=0
    aColecciones = listar_colecciones_db()
    aColeccionesCat = []
    for i in range(len(aColecciones)):
        aColeccionesCat.append(  (aColecciones[i],lista_indices(aColecciones[i]))  )

    if request.method == "POST" and request.POST['drop2']:
        variable, collection = request.POST['drop2'].split('+')
        Variable, Contador, Moda, Total = grafico2.frecuencia(variable, collection)
    return render(request, "Integracion/graficador.html",{ "Variable":Variable,"Contador":Contador,"Moda":Moda,"Total":Total, 'lista_cd_sub':aColeccionesCat})

def buscador_paciente(request, paciente):
    np = paciente
    #medicos, hospitales, profesionales, info, sesiones
    v0,c0,v1,c1,v2,c2, info, sesiones, cant = paciente_stats.frecuencia(paciente)
    print(v0,c0)
    return render(request, "Integracion/buscador.html",{"np":np, "v0": v0, "c0": c0, "v1":v1, "c1":c1, "v2":v2, "c2":c2, "info":info,"sesiones":sesiones, "cant":cant})
