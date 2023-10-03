from django.shortcuts import render

def solicitacao_view(request):    
    return render(request, 'solicitacao/solicitacao.html')
