# Generated by Django 4.1.2 on 2022-10-06 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientesAPP', '0009_departamento_cod_departamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_eapb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tipo_eapb', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Eapb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_eapb', models.CharField(max_length=6)),
                ('cod_habilitacion', models.CharField(max_length=12)),
                ('nombre', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=12)),
                ('nit_dv', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('representante', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1)),
                ('municipio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.municipio')),
                ('tipo_eapb', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.tipo_eapb')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='eapb',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='pacientesAPP.eapb'),
        ),
    ]
