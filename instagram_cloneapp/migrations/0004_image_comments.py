# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_cloneapp', '0003_remove_image_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.CharField(default=6, max_length=80),
            preserve_default=False,
        ),
    ]
