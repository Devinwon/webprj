# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_auto_20170610_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.URLField(default='/static/images/default.png'),
        ),
    ]
