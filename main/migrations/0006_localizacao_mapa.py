# Generated by Django 4.2.2 on 2023-07-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_banner_auditorio_banner_jardim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao_mapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=300)),
                ('mapa', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': '3.4 Localizacao/ mapa',
            },
        ),
    ]
