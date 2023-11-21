from django.db import models

TIPO_CONTA_CHOICES = (
    ('condominio', 'Condomínio'),
    ('area_comum', 'Área Comum'),
)

class registro_cobranca(models.Model):
    data = models.DateField()
    tipo_conta = models.CharField(max_length=30, choices=TIPO_CONTA_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    boleto = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'registro_cobranca'
