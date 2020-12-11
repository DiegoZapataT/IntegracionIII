from pymongo import MongoClient
from bson.json_util import loads
from nltk import flatten
from bson import json_util
import json
import os
import collections
from statistics import multimode


client = MongoClient('mongodb://localhost')

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
    DataBase = open(Dir1)
except:
    DataBase = open(Dir2)

#se abre el archivo JSON para almacenarlo
DataBase = str(json.load(DataBase))
DataBase = DataBase.replace('$oid','id') #reemplazamos el id
DataBase = eval(DataBase)
coleccion.insert_many(DataBase)

#Revisa lo que se envia desde el html para las consultas
def Ruta(Consulta):
    if Consulta == 'nombre_sesion' or Consulta == 'fecha' or Consulta  == 'nombre_profesional' or Consulta  == 'profesion' or Consulta  == 'centro_salud':
        Consulta  == 'sesiones_medica.'+Consulta 

    if Consulta  == 'tipo' or Consulta  == 'clave' or Consulta  == 'valor':
        Consulta  = 'sesiones_medica.arquetipos.'+Consulta 
    return Consulta 

def Frecuencia(Consulta ):
    Variable = []
    VariableRecibida = Consulta  
    Moda=[]
    Total=0
    ConsultaMongo = []

    Consulta  = Ruta(Consulta )


    #Dependiendo lo que se pida desde el formulario, se crea una consulta distinta
    if Consulta  == 'nombre':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$nombre"},}}
    
    if Consulta  == 'apellidos':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$apellidos"},}}

    if Consulta  == 'rut':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$rut"},}}

    if Consulta  == 'direccion':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$direccion"},}}

    if Consulta  == 'fecha_nacimiento':
        ConsultaGrupo = {"$group": { "_id": "$_id", VariableRecibida: {"$push": "$fecha_nacimiento"},}}
    
    if Consulta  == 'ciudad':
        ConsultaGrupo = {"$group": { "_id": "$_id", VariableRecibida: {"$push": "$ciudad"},}} 
              
    if Consulta  == 'nombre_sesion':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$sesiones_medica.nombre_sesion"},}}

    if Consulta  == 'fecha':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$sesiones_medica.fecha"},}}

    if Consulta  == 'nombre_profesional':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$sesiones_medica.nombre_profesional"},}}
    
    if Consulta  == 'profesion':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$sesiones_medica.profesion"},}}

    if Consulta  == 'centro_salud':
        ConsultaGrupo = { "$group": { "_id": "$_id", VariableRecibida: {"$push": "$sesiones_medica.centro_salud"},}}


    #Order By: ASC
    ConsultaOrdenada = {'$sort':{'_id':1}}
    print('diccionaro grupo: ', ConsultaGrupo)

    ConsultaMongo.append(ConsultaGrupo)
    print(ConsultaMongo)

    #se envia la consulta a mongo y luego se recorre para guardar los resultados que se obtengan de la misma
    respuesta = db.arquetipos.aggregate(ConsultaMongo)
    for enviar in respuesta:
        Variable.append(enviar[VariableRecibida])

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