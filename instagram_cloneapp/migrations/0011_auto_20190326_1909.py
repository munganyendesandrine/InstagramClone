# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_cloneapp', '0010_auto_20190326_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='like',
            new_name='likes',
        ),
    ]