# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nap_parser_app', '0008_auto_20171129_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='stock_options',
            field=models.TextField(max_length=2000),
        ),
    ]
