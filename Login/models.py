from django.db import models

# Create your models here.

class UserProfile(models.Model):
    nome = models.CharField(max_length=100)
    nome_usuario = models.CharField(max_length=50, unique=True)
    apartamento = models.CharField(max_length=10)
    tipo_usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)

    class Meta:
            db_table='registro_usuario'
