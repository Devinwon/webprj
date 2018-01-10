# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'male', max_length=10, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('age', models.CharField(max_length=3, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True)),
                ('mobilenumber', models.IntegerField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(default=b'male', max_length=10, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('age', models.CharField(max_length=3, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(null=True)),
                ('mobilenumber', models.IntegerField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to=b'photos/%Y/%m/%d', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
