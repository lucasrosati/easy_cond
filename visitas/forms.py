from django import forms
from .models import visita

class VisitaForm(forms.ModelForm):
    class Meta:
        model = visita
        fields = ['nome', 'cpf', 'tipo_usuario']