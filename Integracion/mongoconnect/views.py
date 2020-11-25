from django.http import HttpResponse
from django.shortcuts import render
from mongoconnect.models import Historial, Prueba1
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps
import pymongo
# Create your views here.
@csrf_exempt
def add_post(request):
    comment = request.POST.get("comment").split(",")
    tags = request.POST.get("tags").split(",")
    post = Posts(post_title = request.POST.get("post_title"), post_description = request.POST.get("post_description"), comment = comment, tags = tags, user_details = user_details)
    post.save()
    return HttpResponse("Inserted")

def update_post(request, id):
    pass

def delete_post(request, id):
    pass

def read_post(request, id):
    post = Posts.objects.get(_id=ObjectId(id))
    stringval = "Post Title "+ post.post_title +"Comentario: "+ post.comment[0]
    return HttpResponse(stringval)

def read_post_all(request):
    posts = Posts.objects.all()
    stringval = ""
    for post in posts:
        stringval += "<h1> Post Title "+ post.post_title +"Comentario: "+ post.comment[0]+"<br> <h1>"
    print (stringval)
    return HttpResponse(stringval)

def getData(request):
    data = Historial.objects.all()
    return data

def getData1(request):
    m = []
    data = Prueba1.objects.all()
    for d in data:
        for i in range(len(d.dias)):
            m.append((d.dias[i],d.casos[i]))
    return m

def listar_colecciones_db(request):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db"]
    mycol = mydb["mongoconnect_historial"]
    filter = {"name": {"$regex": r"^(?!system\.)"}}
    #filter = {"name": "mongoconnect_historial"}
    lista_colecciones = mydb.list_collection_names(include_system_collections=False, filter=filter)

    milista = []
    for i in lista_colecciones:
        if "mongoconnect" in i:
            milista.append(i[13:])

    l_datosd = listar_documento_col("mongoconnect_historial", mydb)
    l_datosc = listar_datos_col("mongoconnect_historial", mydb)
    return milista, l_datosd, l_datosc

def listar_datos_col(collect_name, mydb):
    mycol = mydb[collect_name]
    mi_col = mycol.find({})
    l_mi_col = list(mi_col)
    colls_pretty = dumps(l_mi_col,indent =4)
    return colls_pretty

def listar_documento_col(collect_name, mydb):
    mycol = mydb[collect_name]
    mi_doc = mycol.find_one({})
    #mi_doc = mycol.find({})
    #mi_doc = mi_doc[0]
    l_mi_doc = list(mi_doc)
    doc_pretty = dumps(l_mi_doc,indent =4)
    return doc_pretty

def input_nombre_c():
    return 1