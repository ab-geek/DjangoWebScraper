# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20160518_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripadvisorattraction',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
