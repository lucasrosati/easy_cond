from django.shortcuts import render

def lista_funcionarios_view(request):
    return render(request, 'lista_funcionarios/lista.html')
