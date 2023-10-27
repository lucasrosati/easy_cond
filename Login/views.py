from django.shortcuts import render
from Login.models import UserProfile
from django.http import JsonResponse

def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nome_usuario = request.POST.get('nome_usuario')  # Nome do campo corrigido
        senha = request.POST.get('senha')
        apartamento = request.POST.get('apartamento')
        tipo_usuario = request.POST.get('tipo_usuario')  # Nome do campo corrigido
        
        novoUsuario = UserProfile(nome=nome, nome_usuario=nome_usuario, apartamento=apartamento, tipo_usuario=tipo_usuario, senha=senha)

        try:
            novoUsuario.save()
            return JsonResponse({"message": "Dados salvos com sucesso"})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    return render(request, 'login/pagina_de_cadastro.html')

def cadastro_view(request):
    return render(request, 'login/cadastro.html')

def pagina_inicial(request):
    return render(request, 'login/pagina_de_login.html')

def pagina_de_login_view(request):
    return render(request, 'login/pagina_de_login.html')
