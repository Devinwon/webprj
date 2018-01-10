# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-02 06:15
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mark', models.IntegerField(default=0)),
                ('ph_no', models.IntegerField(null=True)),
                ('rmin', models.CharField(default=50, max_length=2, null=True)),
                ('rsec', models.CharField(default=10, max_length=2, null=True)),
            ],
        ),
    ]
