# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160508_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookpage',
            name='crawl_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
