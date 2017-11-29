# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nap_parser_app', '0005_auto_20171129_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='currency',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='price',
            name='stock_options',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
