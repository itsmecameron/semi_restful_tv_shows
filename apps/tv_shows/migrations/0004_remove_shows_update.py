# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-19 23:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0003_auto_20190619_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shows',
            name='update',
        ),
    ]
