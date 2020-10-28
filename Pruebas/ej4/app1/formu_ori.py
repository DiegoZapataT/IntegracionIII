from django import forms

class Valorform(forms.Form):
    Nombres = forms.CharField(max_length = 100)
    Apellidos = forms.SlugField()
    Profesor = forms.BooleanField()
    Numero_Ip = forms.GenericIPAddressField()
    Foto = forms.FileField()
    Curso = forms.ChoiceField(choices = (('1','Base de Datos'),('2','Desarrollo Web'),('3','Algebra'),('4','Taller III')))    