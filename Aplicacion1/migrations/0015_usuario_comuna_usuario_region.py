# Generated by Django 4.2.5 on 2023-11-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0014_preguntas_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='comuna',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Comuna'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Región'),
        ),
    ]
