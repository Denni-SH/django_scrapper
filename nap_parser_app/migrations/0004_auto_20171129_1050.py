# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nap_parser_app', '0003_auto_20171129_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='site_product_id',
            field=models.CharField(max_length=100),
        ),
    ]
