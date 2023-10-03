from django.shortcuts import render

def reserva_view(request):
    return render(request, 'reserva/reserva.html')

def legenda_view(request):
    return render(request, 'reserva/legenda.html')

def calendario_view(request):
    return render(request, 'reserva/calendario.html')
