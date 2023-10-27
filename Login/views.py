from django.shortcuts import render
from Login.models import UserProfile

# Create your views here.

def cadastro_usuario(request):
    if request.method == 'POST':
        print('Dados recebidos no servidor', request.POST)
        nome = request.POST.get('nome')
        nome_de_usuario = request.POST.get('user')
        senha = request.POST.get('senha')
        apartamento = request.POST.get('apartamento')
        tipo_de_usuario = request.POST.get('tipoUsuario')
        
        
        
        novoUsuario = UserProfile(nome = nome, nome_de_usuario = nome_de_usuario, apartamento = apartamento, tipo_de_usuario = tipo_de_usuario, senha = senha)
        
        try:
            novoUsuario.save()
            print("Dados salvos com sucesso")
        except:
            print("Erro ao salvar dados")

        return render(request, 'login/cadastro.html')
    return render(request, 'login/pagina_de_cadastro.html')    

#nome = nome
#nome de usuario = user
#senha = senha
#apartamento = apartamento
#tipo de usuario = tipoUsuario


def cadastro_view(request):
    return render(request, 'login/cadastro.html')

def pagina_inicial(request):
    return render(request, 'login/cadastro.html')

def pagina_de_login_view(request):
    return render(request, 'login/pagina_de_login.html')