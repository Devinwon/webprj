# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-04 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[(b'mcq', b'mcq'), (b'fill', b'fill'), (b'code', b'code')], default=b'mcq', max_length=3),
        ),
    ]
