# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-26 12:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_cloneapp', '0009_auto_20190326_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='likes',
            new_name='like',
        ),
    ]