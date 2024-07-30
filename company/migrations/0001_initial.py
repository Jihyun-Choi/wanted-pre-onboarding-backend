# Generated by Django 5.0.7 on 2024-07-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("company_name", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("region", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Company",
                "verbose_name_plural": "Companies",
                "db_table": "company",
            },
        ),
    ]
