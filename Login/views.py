from django.shortcuts import render
from django.http import JsonResponse
from .models import UserProfile
from django.contrib.auth.views import LoginView


# Define a sua visualização personalizada para login
class CustomLoginView(LoginView):
    template_name = 'pagina_de_login.html'

# Visualização para cadastrar um novo usuário
def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nome_usuario = request.POST.get('nome_usuario')
        senha = request.POST.get('senha')
        apartamento = request.POST.get('apartamento')
        tipo_usuario = request.POST.get('tipo_usuario')

        # Verificar se o usuário já existe no banco de dados
        usuario_existe = UserProfile.objects.filter(nome_usuario=nome_usuario).exists()
        if usuario_existe:
            return JsonResponse({'error': 'Este nome de usuário já está em uso. Por favor, escolha outro.'})

        novoUsuario = UserProfile(nome=nome, nome_usuario=nome_usuario, apartamento=apartamento, tipo_usuario=tipo_usuario, senha=senha)

        try:
            novoUsuario.save()
            return JsonResponse({"message": "Dados salvos com sucesso"})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return render(request, 'login/pagina_de_cadastro.html')

# Outras visualizações que você já tinha definido
def cadastro_view(request):
    return render(request, 'login/cadastro.html')

def pagina_inicial(request):
    return render(request, 'login/pagina_de_login.html')

def verificar_usuario(request):
    if request.method == 'GET':
        nome_usuario = request.GET.get('nome_usuario')
        # Faça a verificação do usuário no banco de dados
        # Se o usuário já existir, retorne uma resposta JSON adequada
        # Caso contrário, retorne uma resposta JSON apropriada
        # Exemplo:
        if UserProfile.objects.filter(nome_usuario=nome_usuario).exists():
            return JsonResponse({"mensagem": "Usuário já existe"})
        else:
            return JsonResponse({"mensagem": "Usuário disponível"})


def pagina_de_login_view(request):
    return render(request, 'login/pagina_de_login.html')
