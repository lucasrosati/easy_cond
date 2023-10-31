# Generated by Django 4.2.4 on 2023-10-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="solicitacao_servico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "local",
                    models.CharField(
                        choices=[
                            ("academia", "Academia"),
                            ("campo_de_futebol", "Campo de Futebol"),
                            ("quadra_de_tenis", "Quadra de Tênis"),
                            ("espaco_gourmet", "Espaço Gourmet"),
                            ("salao_de_festas", "Salão de Festas"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "tipo_servico",
                    models.CharField(
                        choices=[("manutencao", "Manutenção"), ("limpeza", "Limpeza")],
                        max_length=20,
                    ),
                ),
                ("comentario", models.TextField()),
            ],
            options={
                "db_table": "solicitacoes_de_servico",
            },
        ),
    ]