# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20170610_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.URLField(default='http://semantic-ui.com/images/avatar/small/matt.jpg'),
        ),
    ]
