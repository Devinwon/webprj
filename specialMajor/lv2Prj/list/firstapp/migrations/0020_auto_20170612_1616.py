# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0019_auto_20170612_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='url_img',
        ),
        migrations.AddField(
            model_name='article',
            name='url_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
