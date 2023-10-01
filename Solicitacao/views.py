from django.shortcuts import render

def solicitacao_view(request):    
    return render(request, 'Solicitacao/solicitacao.html')
