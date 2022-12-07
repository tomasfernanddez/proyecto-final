from django import forms
from ejemplo.models import Familiar

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'placeholder': 'Busque algo...'}))

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'fecha', 'numero_pasaporte']