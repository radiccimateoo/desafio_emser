# Generated by Django 4.1.3 on 2022-12-05 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0005_tablapelicula_persona_tablapremio_pelicula_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablapremio',
            name='cantidad_premios_ganados',
        ),
    ]
