# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nap_parser_app', '0009_auto_20171129_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
