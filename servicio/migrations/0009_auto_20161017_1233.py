# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0008_auto_20161017_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='fecha_de_inicio_de_servicio',
            new_name='inicio_de_servicio',
        ),
    ]
