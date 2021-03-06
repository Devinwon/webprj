# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0029_auto_20170618_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.FileField(default='/static/images/default.png', upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='realname',
            field=models.CharField(blank=True, default='普通用户', max_length=50, null=True),
        ),
    ]
