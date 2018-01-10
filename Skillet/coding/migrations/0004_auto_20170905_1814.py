# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-05 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0003_auto_20170904_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='codequestiontestcase',
            name='problem_statement',
            field=models.TextField(default='<p>ram x amount of money</p>'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='codequestiontestcase',
            name='answer_file',
            field=models.FileField(upload_to='answers'),
        ),
        migrations.AlterField(
            model_name='codequestiontestcase',
            name='testcase_file',
            field=models.FileField(upload_to='testcases'),
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='user_output',
            field=models.FileField(upload_to='user_submission'),
        ),
    ]
