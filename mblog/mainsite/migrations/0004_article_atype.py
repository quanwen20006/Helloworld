# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-12 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20171010_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='atype',
            field=models.CharField(choices=[('auto', '\u81ea\u52a8\u5316\u6d4b\u8bd5'), ('safe', '\u5b89\u5168\u6d4b\u8bd5'), ('per', '\u6027\u80fd\u6d4b\u8bd5'), ('busi', '\u4e1a\u52a1')], default='auto', max_length=10),
        ),
    ]
