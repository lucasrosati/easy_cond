# Generated by Django 4.2.4 on 2023-10-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CamerasProfile",
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
                ("numero", models.CharField(max_length=2)),
                ("area", models.CharField(max_length=50)),
                ("url", models.CharField(max_length=500)),
            ],
            options={
                "db_table": "registro_cameras",
            },
        ),
    ]