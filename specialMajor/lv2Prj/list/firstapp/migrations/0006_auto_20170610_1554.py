# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20170610_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]
