# Generated by Django 4.2.4 on 2023-11-21 19:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adicionar_funcionario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registro_funcionario",
            name="horario",
            field=models.CharField(
                choices=[
                    ("matutino/vespertino", "Matutino/Vespertino"),
                    ("vespertino/noturno", "Vespertino/Noturno"),
                    ("noturno/matutino", "Noturno/Matutino"),
                ],
                max_length=30,
            ),
        ),
    ]
