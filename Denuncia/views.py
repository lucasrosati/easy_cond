from django.shortcuts import render, redirect
from .models import registro_denuncia

def fazer_denuncia(request):
    context = {}  # Dicionário para armazenar as mensagens e outros contextos
    if request.method == 'POST':
        local = request.POST.get('local')
        tipo_infracao = request.POST.get('tipo_infracao')
        unidade = request.POST.get('unidade')
        comentario = request.POST.get('comentario')

        if not local or not tipo_infracao or not unidade:
            context['error'] = 'Campos obrigatórios não preenchidos'
        else:
            registro_denuncia.objects.create(
                local=local,
                tipo_infracao=tipo_infracao,
                unidade=unidade,
                comentario=comentario
            )
            context['success_message'] = 'Denúncia enviada com sucesso!'
    
    return render(request, 'denuncia/denuncia.html', context)