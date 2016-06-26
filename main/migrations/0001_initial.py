# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('abbr', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CrawlerRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('records_downloaded', models.CharField(max_length=25)),
                ('records_merged', models.CharField(max_length=25)),
                ('records_new', models.CharField(max_length=25)),
                ('bytes_downloaded', models.CharField(max_length=25)),
                ('start_time', models.CharField(max_length=25)),
                ('end_time', models.CharField(max_length=25)),
                ('mailed', models.BooleanField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.TextField()),
                ('scraper', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('abbr', models.CharField(max_length=5)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Country')),
            ],
        ),
        migrations.CreateModel(
            name='TripAdvisorAttraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('website', models.TextField()),
                ('email', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.TextField()),
                ('keywords', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TripAdvisorCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cat', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TripAdvisorLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.State')),
            ],
        ),
        migrations.AddField(
            model_name='tripadvisorattraction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TripAdvisorCat'),
        ),
        migrations.AddField(
            model_name='tripadvisorattraction',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.State'),
        ),
        migrations.AddField(
            model_name='crawlerrecord',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Site'),
        ),
    ]