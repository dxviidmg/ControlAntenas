# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infraestructura', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linea',
            old_name='pago',
            new_name='mensualidad',
        ),
    ]