# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_comment_belong_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.CharField(default='/static/images/img5.jpg', max_length=250),
        ),
    ]
