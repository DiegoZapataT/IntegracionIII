from django import forms

class FormUsuario(forms.Form):
    nombre= forms.CharField(max_length=100)
    apellido= forms.CharField(max_length=100)
    correo= forms.EmailField()
    fono= forms.CharField(max_length=100)