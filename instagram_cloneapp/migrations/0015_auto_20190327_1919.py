# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_cloneapp', '0014_auto_20190327_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='likes',
            new_name='like',
        ),
    ]