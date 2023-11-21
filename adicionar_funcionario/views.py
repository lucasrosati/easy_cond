from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FuncionarioForm

def adicionar_funcionario_view(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário adicionado com sucesso!')
            return redirect('adicionar_funcionario')  # Redireciona para a mesma view
    else:
        form = FuncionarioForm()

    return render(request, 'adicionar_funcionario/adicionar_funcionario.html', {'form': form})

