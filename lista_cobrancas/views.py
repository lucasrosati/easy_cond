from django.shortcuts import render
from adicionar_cobranca.models import registro_cobranca 

def lista_cobrancas_view(request):
    cobrancas = registro_cobranca.objects.all()  
    return render(request, 'lista_cobrancas/lista_cobrancas.html', {'cobrancas': cobrancas})
