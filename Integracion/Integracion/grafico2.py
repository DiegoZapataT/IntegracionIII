from statistics import multimode, mode
from pymongo import MongoClient
from bson.son import SON


#conecta unicamente a las colecciones existetes en la base de datos cuyos nombres comiencen
#con 'mongoconnect_', el cual es un filtro temporal, mientras
#no se configure un usuario para la aplicación (con permisos limitados
#sobre la bd)
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["historiales"]

# devuelve 2 arreglos ( o listas) planos
# el arreglo Variable con los nombres de la variable a buscar y
# el arreglo Contador con la cantidad de ocurrencias de cada valor de Variable
def frecuencia(variable, collection):
    mycol = mydb[ collection]
    variable = '$'+variable
    consulta = [
           {"$unwind": variable},
           {"$group": {"_id": variable, "count": {"$sum": 1}}},
           {"$sort": SON([("count", -1), ("_id", -1)])}
    ]

    respuesta = list(mycol.aggregate(consulta))
    #print (respuesta)
    # respuesta es un arreglo con el formato [{'llave':2,'llave':5}, {}, ...]

    Variable = []
    Contador = []
    Moda = []
    for i in respuesta:
        Variable.append(i['_id'])
        Contador.append(i['count'])
        #print ('la variable '+i['_id']+' se repite '+str(i['count']))
    #print(Variable)

    consulta2 = mycol.count()
    Total = consulta2

    # en caso de que el total fuera la cantidad de registros unicos
    Totalunicos = len(Variable)

    # Calcula la moda usando multimode
    if Total>0:
        #Moda = multimode(Variable)
        Moda = mode(Variable)

    return Variable, Contador, Moda, Total#, Totalunicos