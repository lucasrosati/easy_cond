from django.db import models

# Create your models here.

class UserProfile(models.Model):
    nome = models.CharField(max_length=100)
    nome_usuario = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)  # CPF deve ser único
    apartamento = models.CharField(max_length=10)
    tipo_usuario = models.CharField(max_length=20)

    #class Meta:
            #db_table=#nome da tabela criada
