# Generated by Django 4.1.2 on 2022-10-06 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientesAPP', '0006_paciente_estado_paciente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nro_identificacion',
            field=models.CharField(default='', max_length=15),
        ),
    ]