# Generated by Django 5.1 on 2024-08-24 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_categoria_fornecedor_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
    ]
