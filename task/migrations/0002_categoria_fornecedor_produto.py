# Generated by Django 5.1 on 2024-08-24 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='fornecedores/')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('preco_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.PositiveIntegerField()),
                ('tamanho', models.CharField(blank=True, max_length=10, null=True)),
                ('cor', models.CharField(blank=True, max_length=20, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produtos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.categoria')),
            ],
        ),
    ]