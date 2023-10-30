from django.db import models

LOCAL_CHOICES = (
    ('academia', 'Academia'),
    ('campo_de_futebol', 'Campo de Futebol'),
    ('quadra_de_tenis', 'Quadra de Tênis'),
    ('espaco_gourmet', 'Espaço Gourmet'),
    ('salao_de_festas', 'Salão de Festas'),
)

TIPO_INFRACAO = (
    ('barulhe_excessivo', 'Barulho Excessivo'),
    ('dano_ao_patrimõnio', 'Dano ao Patrimônio'),
    ('desrespeito_as_normas', 'Desreipeito às Normas'),
)

# Create your models here.
class registro_denuncia(models.Model):
    local = models.CharField(max_length=20, choices=LOCAL_CHOICES)
    tipo_infracao = models.CharField(max_length=30, choices=TIPO_INFRACAO)
    unidade = models.CharField(max_length=4)
    comentario = models.TextField()

    class Meta:
        db_table = 'registro_denuncia'