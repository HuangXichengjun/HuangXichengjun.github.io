# Generated by Django 5.0.6 on 2024-06-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Remark",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "remark_db",
            },
        ),
    ]
