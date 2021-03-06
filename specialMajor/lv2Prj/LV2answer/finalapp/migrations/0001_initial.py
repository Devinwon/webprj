# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-12 00:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('url_image', models.URLField(blank=True, null=True)),
                ('cover', models.FileField(null=True, upload_to='cover_image')),
                ('editors_choice', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='finalapp.Video'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voted_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
