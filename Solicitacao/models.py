from django.db import models


LOCAL_CHOICES = (
    ('academia', 'Academia'),
    ('campo_de_futebol', 'Campo de Futebol'),
    ('quadra_de_tenis', 'Quadra de Tênis'),
    ('espaco_gourmet', 'Espaço Gourmet'),
    ('salao_de_festas', 'Salão de Festas'),
)

TIPO_SERVICO_CHOICES = (
    ('manutencao', 'Manutenção'),
    ('limpeza', 'Limpeza'),
)

# Create your models here.
class solicitacao_servico(models.Model):
    local = models.CharField(max_length=20, choices=LOCAL_CHOICES)
    tipo_servico = models.CharField(max_length=20, choices=TIPO_SERVICO_CHOICES)
    comentario = models.TextField()

    class Meta:
        db_table = 'solicitacoes_de_servico'
