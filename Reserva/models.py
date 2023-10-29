from django.db import models


ESPAÇO_CHOICES = (
    ('salao_de_festas', 'Salão de Festas'),
    ('campo_de_futebol', 'Campo de Futebol'),
    ('espaco_gourmet', 'Espaço Gourmet'),
    ('quadra_de_tenis', 'Quadra de Tênis'),
)

# Create your models here.
class cadasto_reserva(models.Model):
    espaco_comum = models.CharField(max_length=20, choices=ESPAÇO_CHOICES)
    data_reserva = models.DateField()


class Meta:
    db_table = 'reserva_de_espaco'