
from django.http import HttpResponse
from django.shortcuts import render
from mongoconnect.models import Posts, Prueba1
from django.views.decorators.csrf import csrf_exempt

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

def getData1(request):
    posts = Posts.objects.all()
    stringval = ""
    for post in posts:
        stringval += "<h1> Post Title "+ post.post_title +"Comentario"+ post.comment[0]+"<br> <h1>"
    stringval += "no"
    return stringval

def getData(request):
    m = []
    data = Prueba1.objects.all()
    for d in data:
        for i in range(len(d.dias)):
            m.append((d.dias[i],d.casos[i]))
    return m

