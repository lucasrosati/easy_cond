from django.shortcuts import render

# Create your views here.

def pagina_de_login_view(request):
    return render(request, 'login/pagina_de_login.html')

def cadastro_view(request):
    return render(request, 'login/cadastro.html')

def pagina_de_cadastro_view(request):
    return render(request, 'login/pagina_de_cadastro.html')

def pagina_inicial(request):
    return render(request, 'login/cadastro.html')