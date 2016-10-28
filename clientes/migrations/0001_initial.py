# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=30)),
                ('numero_exterior', models.CharField(max_length=10)),
                ('numero_interior', models.CharField(blank=True, max_length=10, null=True)),
                ('colonia', models.CharField(max_length=20)),
                ('municipio', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('codigo_postal', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=10)),
                ('fecha_de_nacimiento', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='direccion',
            name='perfil',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clientes.Perfil'),
        ),
    ]
