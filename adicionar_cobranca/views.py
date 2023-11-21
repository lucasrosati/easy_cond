from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CobrancaForm

def adicionar_cobranca_view(request):
    if request.method == 'POST':
        form = CobrancaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cobrança adicionada com sucesso!')
            return redirect('adicionar_cobranca')  
    else:
        form = CobrancaForm()

    return render(request, 'adicionar_cobranca/adicionar_cobranca.html', {'form': form})
