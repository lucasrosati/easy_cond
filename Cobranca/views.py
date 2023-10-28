from django.shortcuts import render

def cobranca_view(request):
    return render(request, 'cobranca/cobranca.html')
