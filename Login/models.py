from django.db import models

class UserProfile(models.Model):
    nome = models.CharField(max_length=100)
    nome_usuario = models.CharField(max_length=50, unique=True)  # Nome do campo corrigido
    apartamento = models.CharField(max_length=10)
    tipo_usuario = models.CharField(max_length=20)  # Nome do campo corrigido
    senha = models.CharField(max_length=50)

    class Meta:
        db_table = 'registro_usuario'
