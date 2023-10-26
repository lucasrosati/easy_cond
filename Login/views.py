from django.shortcuts import render
from Login.models import UserProfile

# Create your views here.

def pagina_de_login_view(request):
    if request.method == 'POST':
        print('Dados recebidos no servidor', request.POST)
        nome = request.POST.get('nome')
        nome_de_usuario = request.POST.get('user')
        senha = request.POST.get('senha')
        apartamento = request.POST.get('apartamento')
        tipo_de_usuario = request.POST.get(tipoUsuario)



#nome = nome
#nome de usuario = user
#senha = senha
#apartamento = apartamento
#tipo de usuario = tipoUsuario


def cadastro_view(request):
    return render(request, 'login/cadastro.html')

def pagina_de_cadastro_view(request):
    return render(request, 'login/pagina_de_cadastro.html')

def pagina_inicial(request):
    return render(request, 'login/cadastro.html')