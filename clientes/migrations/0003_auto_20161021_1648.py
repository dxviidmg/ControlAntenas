# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20161004_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(max_length=30),
        ),
    ]
