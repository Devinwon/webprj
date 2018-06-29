# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='school',
            field=models.CharField(default=b'New Horizon', max_length=10),
        ),
        migrations.AddField(
            model_name='teacherprofile',
            name='school',
            field=models.CharField(default=b'New Horizon', max_length=10),
        ),
    ]
