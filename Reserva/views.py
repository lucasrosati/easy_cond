from django.shortcuts import render

def reserva_view(request):
    return render(request, 'Reserva/reserva.html')

def legenda_view(request):
    return render(request, 'Reserva/legenda.html')

def calendario_view(request):
    return render(request, 'Reserva/calndario.html')
