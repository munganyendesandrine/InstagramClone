# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_cloneapp', '0008_auto_20190326_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='like',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]