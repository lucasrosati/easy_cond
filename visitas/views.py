from django.shortcuts import render, redirect
from .models import visita

def cadastro_visita_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        tipo_usuario = request.POST.get('tipo_usuario')  # Ajuste o nome do campo para corresponder ao HTML

        if not nome or not cpf or not tipo_usuario:
            # Adicione algum código de manipulação de erro aqui
            return render(request, 'cadastro_visita.html', {'error': 'Campos obrigatórios não preenchidos'})

        visita.objects.create(
            nome=nome,
            cpf=cpf,
            tipo_usuario=tipo_usuario
        )

        return redirect('/menu/')  # Redirecione para o menu após o cadastro bem-sucedido

    return render(request, 'cadastro_visita.html')

def visitas_view(request):
    return render(request, 'visitas/cadastro_visitas.html')
