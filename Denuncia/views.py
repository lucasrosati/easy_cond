from django.shortcuts import render

def denuncia_view(request):
    return render(request, 'denuncia/denuncia.html')
