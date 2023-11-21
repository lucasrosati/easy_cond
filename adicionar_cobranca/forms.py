from django import forms
from .models import registro_cobranca, TIPO_CONTA_CHOICES

class CobrancaForm(forms.ModelForm):
    class Meta:
        model = registro_cobranca
        fields = ['data', 'tipo_conta', 'valor', 'boleto']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_conta': forms.Select(choices=TIPO_CONTA_CHOICES, attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'boleto': forms.URLInput(attrs={'class': 'form-control'}),
        }
