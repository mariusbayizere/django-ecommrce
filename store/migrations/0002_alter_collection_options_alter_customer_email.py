# Generated by Django 5.1.7 on 2025-04-08 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="collection",
            options={"ordering": ["Tittle"]},
        ),
        migrations.AlterField(
            model_name="customer",
            name="Email",
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
