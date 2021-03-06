# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0031_auto_20170624_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Article'},
        ),
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='cover_image', verbose_name='封面'),
        ),
    ]
