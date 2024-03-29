# Generated by Django 4.1.5 on 2023-01-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100, null=True, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=100, null=True, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=100, null=True, verbose_name='Placa')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
            ],
        ),
    ]
