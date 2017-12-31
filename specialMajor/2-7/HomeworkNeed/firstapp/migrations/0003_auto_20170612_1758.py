# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20161105_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='img',
            new_name='url_image',
        ),
        migrations.AddField(
            model_name='article',
            name='editors_choice',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='createtime',
            field=models.DateField(auto_now=True),
        ),
    ]
