# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-30 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('footsteps', '0003_auto_20170829_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edit_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='최종 수정 시간'),
        ),
    ]