# Generated by Django 4.1.2 on 2022-10-06 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientesAPP', '0004_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='discapacidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.discapacidad'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estado_civil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.estado_civil'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='etnia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.etnia'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='grupo_rh',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.grupo_rh'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nivel_educativo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.nivel_educativo'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='sexo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.sexo'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
