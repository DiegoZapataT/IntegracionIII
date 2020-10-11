from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    index = open("C:/Users/dzapa/OneDrive/Documentos/GitHub/IntegracionIII/Integracion/Integracion/plantillas/index.html")
    plt   = Template(index.read())
    index.close()

    ctx    = Context()
    pagina = plt.render(ctx)

    return HttpResponse(pagina)

def tutorial(request):

    tutorial = open("C:/Users/dzapa/OneDrive/Documentos/GitHub/IntegracionIII/Integracion/Integracion/plantillas/tutorial.html")
    plt      = Template(tutorial.read())
    tutorial.close()

    ctx    = Context()
    pagina = plt.render(ctx)

    return HttpResponse(pagina)

def moda(request):

    moda     = open("C:/Users/dzapa/OneDrive/Documentos/GitHub/IntegracionIII/Integracion/Integracion/plantillas/moda.html")
    plt      = Template(moda.read())
    moda.close()

    ctx    = Context()
    pagina = plt.render(ctx)

    return HttpResponse(pagina)

def promedio(request):

    promedio = open("C:/Users/dzapa/OneDrive/Documentos/GitHub/IntegracionIII/Integracion/Integracion/plantillas/promedio.html")
    plt      = Template(promedio.read())
    promedio.close()

    ctx      = Context()
    pagina   = plt.render(ctx)

    return HttpResponse(pagina)

def regresionlineal(request):
    
    r_lineal = open("C:/Users/dzapa/OneDrive/Documentos/GitHub/IntegracionIII/Integracion/Integracion/plantillas/regresionlineal.html")
    plt      = Template(r_lineal.read())
    r_lineal.close()

    ctx      = Context()
    pagina   = plt.render(ctx)

    return HttpResponse(pagina)