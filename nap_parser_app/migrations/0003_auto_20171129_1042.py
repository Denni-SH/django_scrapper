# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nap_parser_app', '0002_auto_20171129_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='price',
            name='site_product_id',
            field=models.IntegerField(default=0),
        ),
    ]
