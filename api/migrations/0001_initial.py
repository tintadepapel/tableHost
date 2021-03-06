# Generated by Django 4.0.2 on 2022-02-19 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteOmie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_cliente', models.CharField(max_length=15)),
                ('cenario_fiscal', models.CharField(max_length=30)),
                ('nome_fantasia', models.CharField(max_length=50)),
                ('razao_social', models.CharField(max_length=80)),
                ('cnpj', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoCompleto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_agenda', models.CharField(max_length=30)),
                ('data_agenda', models.DateField()),
                ('data_liberado', models.DateField()),
                ('data_inicio', models.DateField()),
                ('data_expedicao', models.DateField()),
                ('status_pedido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoOmie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pedido', models.IntegerField(unique=True)),
                ('pedido', models.CharField(max_length=8, unique=True)),
                ('inclusao', models.DateTimeField()),
                ('ultima_alteracao', models.DateTimeField()),
                ('previsao_faturamento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PendenciaCompleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VendedorOmie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_vendedor', models.CharField(max_length=15)),
                ('nome_vendedor', models.CharField(max_length=20)),
            ],
        ),
    ]
