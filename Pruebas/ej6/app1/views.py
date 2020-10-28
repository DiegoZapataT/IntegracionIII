from django.shortcuts import render
import matplotlib.pyplot as plt
import random
import io
import urllib, base64
import numpy as np
import pandas as pd

def graf(request):
    csv = pd.read_csv('./datos.csv')
    dataset = []
    k = 0
    for i, (vX, vY) in csv.iterrows(): 
        dataset.append({"vX":vX, "vY":vY})
        k = k + 1

    #x = np.linspace(0, k , 100)
    plt.figure(figsize=(10,7))

    for i in range(0,k):
        #x = np.linspace(0, 30, 100)
        punto = dataset[i]
        #print(punto)
        #print('x=',punto.get('vX'),' y=',punto.get('vY'))
        vx = punto.get('vX')
        vy = punto.get('vY')
        #y = x + np.random.randn(100) 
        print('x= ',vx,'  y= ',vy)

        fig = plt.plot(vx, vy, 'o', markersize=2)

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return render(request,'home.html',{'data':uri})

def home(request):
    return render(request,'home.html')
# Create your views here.

