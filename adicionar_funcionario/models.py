from django.db import models

CARGO_CHOICES = (
    ('gerente', 'Gerente'),
    ('zelador', 'Zelador'),
    ('porteiro', 'Porteiro'),    
)

HORARIO_CHOICES = (
    ('matutino/vespertino', 'Matutino/Vespertino'),
    ('vespertino/noturno', 'Vespertino/Noturno'),
    ('noturno/matutino', 'Noturno/Matutino'),
)

# Create your models here.
class registro_funcionario(models.Model):
    nome = models.TextField(max_length=50)
    cargo = models.CharField(max_length=30, choices=CARGO_CHOICES)
    contato = models.TextField(max_length=20)
    horario = models.CharField(max_length=30, choices=HORARIO_CHOICES)

    class Meta:
        db_table = 'registro_funcionario'
