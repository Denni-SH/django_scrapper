# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nap_parser_app', '0004_auto_20171129_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='site_product_id',
            field=models.IntegerField(default=0),
        ),
    ]
