# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-19 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0002_auto_20190619_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='desc',
            field=models.CharField(default='This is a show', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shows',
            name='update',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
