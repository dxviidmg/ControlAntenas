# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-08 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='paquete',
            name='publico',
            field=models.BooleanField(default=True),
        ),
    ]