from django import forms

class ComprarPerro(forms.Form):
    raza = forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=30)
    imagen = forms.ImageField(required=False)

class BuscarPerro(forms.Form):
    raza = forms.CharField(max_length=30, required=False)
    
