# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infraestructura', '0002_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
