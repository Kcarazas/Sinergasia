# Generated by Django 4.2.5 on 2023-11-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0009_alter_preguntas_max_puntaje_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='retroalimentacion',
            field=models.TextField(blank=True, verbose_name='Retroalimentación'),
        ),
    ]