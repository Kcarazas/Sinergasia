# Generated by Django 4.2.5 on 2023-11-12 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0007_rename_quizuser_preguntasrespondidas_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preguntasrespondidas',
            old_name='usuario',
            new_name='quizuser',
        ),
    ]