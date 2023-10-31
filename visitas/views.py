from django.shortcuts import render, redirect
from .models import visita
from django.contrib import messages

def cadastro_visita_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        tipo_usuario = request.POST.get('tipo_usuario')

        if not nome or not cpf or not tipo_usuario:
            messages.error(request, 'Todos os campos são obrigatórios')
            return render(request, 'visitas/cadastro_visitas.html')
        
        nova_visita, created = visita.objects.get_or_create(
            cpf=cpf,
            defaults={'nome': nome, 'tipo_usuario': tipo_usuario}
        )

        if created:
            messages.success(request, 'Cadastro realizado com sucesso!')
        else:
            messages.info(request, 'Visitante já estava cadastrado. Informações atualizadas.')

        return redirect('menu')

    return render(request, 'visitas/cadastro_visitas.html')


def visitas_view(request):    
    return render(request, 'visitas/cadastro_visitas.html')
