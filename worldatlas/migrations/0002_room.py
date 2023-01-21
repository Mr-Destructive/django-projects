# Generated by Django 4.1.5 on 2023-01-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("worldatlas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=128)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]