# Generated by Django 4.2.2 on 2023-07-05 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_quartos_preco_preco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quartos_preco',
            name='descricao',
        ),
    ]
