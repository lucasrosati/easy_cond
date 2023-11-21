from django import forms
from .models import registro_funcionario, CARGO_CHOICES, HORARIO_CHOICES

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = registro_funcionario
        fields = ['nome', 'cargo', 'contato', 'horario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(choices=CARGO_CHOICES, attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.Select(choices=HORARIO_CHOICES, attrs={'class': 'form-control'}),
        }
