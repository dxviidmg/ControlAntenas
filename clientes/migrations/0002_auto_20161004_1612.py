# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]