# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20160718_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='assets',
        ),
        migrations.DeleteModel(
            name='IP',
        ),
    ]