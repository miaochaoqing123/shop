# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-02 09:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_goodscategorybrand_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
