# Generated by Django 4.2.4 on 2023-11-21 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="registro_cobranca",
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
                ("data", models.DateField()),
                (
                    "tipo_conta",
                    models.CharField(
                        choices=[
                            ("condominio", "Condomínio"),
                            ("area_comum", "Área Comum"),
                        ],
                        max_length=30,
                    ),
                ),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("boleto", models.URLField(blank=True, null=True)),
            ],
            options={
                "db_table": "registro_cobranca",
            },
        ),
    ]
