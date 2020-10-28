from django.shortcuts import render
from . forms import FormUsuario

def index(request):
    submitbutton= request.POST.get("submit")

    nombre=''
    apellido=''
    correo=''
    fono=''

    form= FormUsuario(request.POST or None)
    if form.is_valid():
        nombre= form.cleaned_data.get("nombre")
        apellido= form.cleaned_data.get("apellido")
        correo= form.cleaned_data.get("correo")
        fono= form.cleaned_data.get("fono")


    context= {'form': form, 'nombre': nombre, 'apellido': apellido,
              'correo': correo, 'fono': fono, 'submitbutton': submitbutton}
        
    return render(request, 'index.html', context)

