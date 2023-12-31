# Generated by Django 4.2.4 on 2023-08-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
            ],
        ),
    ]
