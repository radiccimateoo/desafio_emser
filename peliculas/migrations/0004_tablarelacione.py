# Generated by Django 4.1.3 on 2022-11-30 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_delete_tablarelaciones'),
    ]

    operations = [
        migrations.CreateModel(
            name='tablaRelacione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='peliculas.tablapersona')),
            ],
        ),
    ]