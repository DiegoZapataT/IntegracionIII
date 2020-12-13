from pymongo import MongoClient
from bson.son import SON

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["historiales"]
mycol = mydb['arquetipos']

def frecuencia(rut_p):
    pacienterut = str(rut_p)
    #pacienterut = "88640826-8"

    consulta3 = [{"$match": {"rut": pacienterut}},
                 {"$unwind": "$sesiones_medica"},
                 {"$project": {"sesion": "$sesiones_medica", "_id": 0}},
                 {"$project": {"sesion.arquetipos": 0}},
                 {"$sort": SON([("sesion.fecha", -1)])}
                 ]

    sesiones = list(mycol.aggregate(consulta3))
    cantidad_sesiones = len(sesiones)

    consulta0 = {'rut': pacienterut}
    paciente_info = list(mycol.find(consulta0, {"sesiones_medica": 0, "profesionales_que_atendieron": 0, "_id": 0}))[0]

    consulta6 = [{"$match": {"rut": pacienterut}},
                 {"$unwind": "$sesiones_medica"},
                 {"$project": {"sesion": "$sesiones_medica", "_id": 0}},
                 {"$project": {"sesion.arquetipos": 0}},
                 {"$unwind": "$sesion.centro_salud"},
                 {"$group": {"_id": "$sesion.centro_salud", "count": {"$sum": 1}}}
                 ]
    por_hospital = list(mycol.aggregate(consulta6))

    consulta7 = [{"$match": {"rut": pacienterut}},
                 {"$unwind": "$sesiones_medica"},
                 {"$project": {"sesion": "$sesiones_medica", "_id": 0}},
                 {"$project": {"sesion.arquetipos": 0}},
                 {"$unwind": "$sesion.nombre_profesional"},
                 {"$group": {"_id": "$sesion.nombre_profesional", "count": {"$sum": 1}}}
                 ]
    por_medico = list(mycol.aggregate(consulta7))

    consulta8 = [{"$match": {"rut": pacienterut}},
                 {"$unwind": "$sesiones_medica"},
                 {"$project": {"sesion": "$sesiones_medica", "_id": 0}},
                 {"$project": {"sesion.arquetipos": 0}},
                 {"$unwind": "$sesion.profesion"},
                 {"$group": {"_id": "$sesion.profesion", "count": {"$sum": 1}}}
                 ]
    por_profesion_medico = list(mycol.aggregate(consulta8))

    v0 = []; c0 = []
    for i in por_medico:
        v0.append(i['_id'])
        c0.append(i['count'])

    v1 = []; c1 = []
    for i in por_hospital:
        v1.append(i['_id'])
        c1.append(i['count'])

    v2 = []; c2 = []
    for i in por_profesion_medico:
        v2.append(i['_id'])
        c2.append(i['count'])

    return (v0,c0,v1,c1,v2,c2 ,paciente_info, sesiones, cantidad_sesiones)