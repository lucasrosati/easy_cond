from django.shortcuts import render
from adicionar_funcionario.models import registro_funcionario  # Importando o modelo

def lista_funcionarios_view(request):
    funcionarios = registro_funcionario.objects.all()  # Busca todos os funcionários no banco de dados
    return render(request, 'lista_funcionarios/lista.html', {'funcionarios': funcionarios})
