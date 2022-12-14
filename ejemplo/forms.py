from django import forms
from ejemplo.models import Familiar
from ejemplo.models import Auto
from ejemplo.models import Mascota

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'}))


class BuscarAuto(forms.Form):
    marca = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'}))


class BuscarMascota(forms.Form):
    nombre = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'}))


class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'fecha', 'numero_pasaporte']


class AutoForm(forms.ModelForm):
  class Meta:
    model = Auto
    fields = ['marca', 'modelo', 'color', 'patente']


class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'animal', 'raza', 'fecha']