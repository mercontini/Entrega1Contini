from django import forms

class FormDestino(forms.Form):

    provincia = forms.CharField()
    ciudad = forms.CharField()
    codigopostal = forms.IntegerField()


class FormTraslado(forms.Form):   
    tipo= forms.CharField(max_length=30)
    duracion = forms.IntegerField()

class FormActividades(forms.Form):
    tipo = forms.CharField(max_length=30)
    modalidad = forms.CharField(max_length=30)
    duracion = forms.IntegerField()

class FormEmail(forms.Form):
    email = forms.EmailField()

class BusquedaDestino(forms.Form):
    destino=forms.CharField()




