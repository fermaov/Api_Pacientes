# Generated by Django 4.1.2 on 2022-10-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_identificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_tipo_iden', models.CharField(max_length=2)),
                ('nom_tipo_iden', models.CharField(max_length=30)),
            ],
        ),
    ]
