# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galleryToday/')),
                ('image_name', models.CharField(max_length=30)),
                ('image_caption', models.CharField(max_length=30)),
                ('likes', models.IntegerField(max_length=8)),
                ('comments', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['image_name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram_cloneapp.Profile'),
        ),
    ]