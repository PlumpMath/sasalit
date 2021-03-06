# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 10:38
from __future__ import unicode_literals

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170829_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='literature_class_no',
        ),
        migrations.AddField(
            model_name='profile',
            name='joined_classes',
            field=models.ManyToManyField(related_name='joined_class', to='core.ClassTime', verbose_name='수강 수업'),
        ),
        migrations.AlterField(
            model_name='classtime',
            name='code',
            field=models.CharField(default='c02c28aa', help_text='절대 수정하지 마세요!!', max_length=10, verbose_name='수업 코드 (수정금지)'),
        ),
        migrations.AlterField(
            model_name='classtime',
            name='semester',
            field=models.IntegerField(default=1, validators=[core.validators.validate_semester], verbose_name='수업 학기'),
        ),
        migrations.AlterField(
            model_name='classtime',
            name='year',
            field=models.IntegerField(default=2017, validators=[core.validators.validate_year], verbose_name='수업 연도'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='class_no',
            field=models.IntegerField(verbose_name='반'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='join_year',
            field=models.IntegerField(default=2016, verbose_name='입학 년도'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='student_no',
            field=models.IntegerField(verbose_name='번호'),
        ),
    ]
