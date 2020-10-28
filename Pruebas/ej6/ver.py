from django.shortcuts import render
import matplotlib.pyplot as plt
import random
import io
import numpy as np
import pandas as pd


csv = pd.read_csv('./datos.csv')
dataset = []
k = 0
for i, (vX, vY) in csv.iterrows(): 
    dataset.append({"vX":vX, "vY":vY})
    k = k + 1
        
print('k= ',k)
for i in range(0,k):
    data = dataset[i]
    print(data)
    print('x=',data.get('vX'),' y=',data.get('vY'))
    
