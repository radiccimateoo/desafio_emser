# Generated by Django 4.1.3 on 2022-12-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0012_remove_tablapremio_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablapremio',
            name='base',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]