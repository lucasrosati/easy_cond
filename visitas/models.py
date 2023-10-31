from django.db import models


TIPO_USUARIO_CHOICES = (
    ('visitante', 'Visitante'),
    ('funcionario', 'Funcionário'),
)


# Create your models here.
class visita(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  # Supomos que o CPF seja único
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    class Meta:
        db_table = 'cadastro_visita_ou_funcionario'