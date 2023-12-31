# Generated by Django 4.2.2 on 2023-07-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_localizacao_mapa_mapa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos_outras_quartos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='image_quartos')),
                ('titulo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '1.7 Fotos outras/ quartos',
            },
        ),
        migrations.CreateModel(
            name='Fotos_outras_restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='image_restaurante')),
                ('titulo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '1.7 Fotos outras/ restaurante',
            },
        ),
        migrations.CreateModel(
            name='Fotos_quartos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='image_quartos')),
                ('titulo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '1.7 Fotos quartos/ quartos',
            },
        ),
        migrations.CreateModel(
            name='Fotos_restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='image_retaurante')),
                ('titulo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '1.7 Fotos restaurante/ restaurante',
            },
        ),
        migrations.AlterModelOptions(
            name='fotos_all_quartos',
            options={'verbose_name_plural': '2.4 Todas Fotos/ quartos'},
        ),
    ]
