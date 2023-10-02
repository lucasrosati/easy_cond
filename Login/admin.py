from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import UserProfile  # Importe o modelo Person

admin.site.register(UserProfile)  # Registre o modelo Person no admin
