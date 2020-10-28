from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np

def home(request):
    # define eje X
    x = np.linspace(-10, 10, 1000)

    # define una parabola
    y = x**2

    # define el grafico y lo realiza
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # crea una recta
    plt.plot(range(40))

    # convierte grafico a imagen
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    
    # codifica la imagen
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)

    # la muestra en la pagina html
    return render(request,'home.html',{'data':uri}) 

