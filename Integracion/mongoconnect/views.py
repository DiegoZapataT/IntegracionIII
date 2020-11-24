from django.http import HttpResponse
from django.shortcuts import render
from mongoconnect.models import Posts, Prueba1, Historial
from django.views.decorators.csrf import csrf_exempt
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
    #lista_colecciones = ["db_1", "db_2"]
    filter = {"name": {"$regex": r"^(?!system\.)"}}

    lista_colecciones = mydb.list_collection_names(include_system_collections=False, filter=filter)
    print (lista_colecciones)
    return lista_colecciones