# Generated by Django 4.1.3 on 2022-12-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0009_remove_tablapelicula_clob'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablapelicula',
            name='base',
            field=models.BinaryField(blank=True),
        ),
    ]
