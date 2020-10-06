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