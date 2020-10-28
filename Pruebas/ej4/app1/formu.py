from django import forms

class Valorform(forms.Form):
    X = forms.CharField(max_length = 4)
    Y = forms.CharField(max_length = 4)
