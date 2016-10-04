# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-04 16:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0002_adapt_to_ss_manyuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitecode',
            options={'ordering': ('-time_created',), 'verbose_name': '邀请码'},
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'ordering': ('-weight',), 'verbose_name': '节点'},
        ),
        migrations.AlterModelOptions(
            name='ssuser',
            options={'ordering': ('-last_check_in_time',), 'verbose_name': 'SS帐户'},
        ),
        migrations.AlterField(
            model_name='ssuser',
            name='last_check_in_time',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 8, 0), editable=False, null=True, verbose_name='最后签到时间'),
        ),
        migrations.AlterField(
            model_name='ssuser',
            name='last_use_time',
            field=models.IntegerField(db_column='t', default=0, editable=False, help_text='时间戳', verbose_name='最后使用时间'),
        ),
    ]