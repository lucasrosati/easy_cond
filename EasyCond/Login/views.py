from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'login/Pagina_de_login.html')

def cadastro_view(request):
    return render(request, 'login/Cadastro.html')

def pagina_de_cadastro_view(request):
    return render(request, 'login/Pagina_de_cadastro.html')