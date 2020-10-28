from django.shortcuts import render
import matplotlib.pyplot as plt
import random
import io
import urllib, base64
import numpy as np

def home(request):
    n = 50
    for i in range(10):
        x = np.linspace(0, 30, n)

        # se logra un patrón calculando 'y'
        # sumando un valor aleatorio a la 'x'
        y = x + np.random.randn(n) 
        plt.figure(figsize=(10,7))
        fig = plt.plot(x,y,'o',markersize=2)

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'home.html',{'data':uri})
    
# Create your views here.

