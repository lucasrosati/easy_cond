from django.contrib import admin

# Register your models here.

from .models import visita  # Importe o modelo Person

admin.site.register(visita)  # Registre o modelo Person no admin
