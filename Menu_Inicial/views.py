from django.shortcuts import render

def menu_view(request):
    return render(request, 'Menu_inicial/menu.html')
