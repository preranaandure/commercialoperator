# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-01 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0117_remove_park_visible_to_external'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='visible_to_external',
            field=models.BooleanField(default=True),
        ),
    ]
