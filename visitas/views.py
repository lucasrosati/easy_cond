from django.shortcuts import render

def visitas_view(request):
    return render(request, 'visitas/cadastro_visitas.html') 