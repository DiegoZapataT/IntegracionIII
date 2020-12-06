from pymongo import MongoClient
from bson.json_util import loads
from nltk import flatten
from bson import json_util
import json
import os
import collections
from statistics import multimode

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

#se crea la base de datos y se conecta
db = client['historiales']
coleccion = db['arquetipos']
coleccion.drop() 

#Directorio 
Dir  = os.getcwd()
Dir1 = Dir+'\\Integracion\\historial.json'
Dir2 = Dir+'\\hitorial.json'

#Se abre a travez de varias rutas distintas para asegurar su funcionamiento
try: 
    file = open(Dir1)
except:
    file = open(Dir2)

#se abre el archivo JSON para almacenarlo
file = str(json.load(file))
file = file.replace('$oid','id') #reemplazamos el id
file = eval(file)

#se insertan los datos 
coleccion.insert_many(file)

#Revisa lo que se envia desde el html para las consultas
def Ruta(Var):
    if Var == 'nombre_sesion' or Var == 'fecha' or Var == 'nombre_profesional' or Var == 'profesion' or Var == 'centro_salud':
        Var == 'sesiones_medica.'+Var

    if Var == 'tipo' or Var == 'clave' or Var == 'valor':
        Var = 'sesiones_medica.arquetipos.'+Var
    return Var

def Frecuencia(Var):
    Variable = []
    OVar = Var 
    Moda=[]
    Total=0
    Consulta = []

    Var = Ruta(Var)


    #Dependiendo lo que se pida desde el formulario, se crea una consulta distinta
    if Var == 'nombre':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$nombre"},}}
    
    if Var == 'apellidos':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$apellidos"},}}

    if Var == 'rut':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$rut"},}}

    if Var == 'direccion':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$direccion"},}}
    
    if Var == 'nombre_sesion':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$sesiones_medica.nombre_sesion"},}}

    if Var == 'fecha':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$sesiones_medica.fecha"},}}

    if Var == 'nombre_profesional':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$sesiones_medica.nombre_profesional"},}}
    
    if Var == 'profesion':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$sesiones_medica.profesion"},}}

    if Var == 'centro_salud':
        ConsultaGrupo = { "$group": { "_id": "$_id", OVar: {"$push": "$sesiones_medica.centro_salud"},}}


    #Order By: ASC
    ConsultaOrdenada = {'$sort':{'_id':1}}
    print('diccionaro grupo: ', ConsultaGrupo)

    Consulta.append(ConsultaGrupo)
    print(Consulta)

    #se envia la consulta a mongo y luego se recorre para guardar los resultados que se obtengan de la misma
    respuesta = db.arquetipos.aggregate(Consulta)
    for enviar in respuesta:
        Variable.append(enviar[OVar])

    #los valores del arreglo a un arreglo unidimensional para enviar a java
    Variable = flatten(Variable)

    #Se cambian las, por . para evitar conflictos con JavaScript
    for i in range(0,len(Variable)):
        Variable[i] = Variable[i].replace(",",".")

    #se crea un arreglo que cuente las veces que se repite cada variable
    Contador = list(collections.Counter(Variable).values())
    
    print("Data :",Variable)
    print("Contador:",Contador)

    #Calcula la moda usando multimode
    if len(Variable)>0:
        Moda = multimode(Variable)
        print('moda: ',Moda)

    #Calculo la cantidad de registros
    for i in Contador:
        Total+=i
    
    #Elimina valores que esten repetidos de manera que se filtren los mismos
    Variable = list(dict.fromkeys(Variable))
    Variable = json.dumps(Variable)

    return Variable, Contador, Moda, Total