# Generated by Django 4.1.3 on 2022-12-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0011_tablapremio_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablapremio',
            name='imagen',
        ),
    ]
