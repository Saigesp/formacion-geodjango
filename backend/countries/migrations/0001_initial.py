# Generated by Django 4.2.1 on 2023-05-11 11:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=255)),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(
                        db_index=True, srid=4326
                    ),
                ),
            ],
        ),
    ]