# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20171020_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
