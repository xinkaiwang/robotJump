# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketinfo',
            name='last_sync_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='bucketinfo',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
