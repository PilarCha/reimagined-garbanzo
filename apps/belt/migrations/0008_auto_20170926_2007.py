# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0007_auto_20170926_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='favorite_Quote',
        ),
        migrations.AddField(
            model_name='quote',
            name='favorite_Quote',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_favorited', to='belt.User'),
            preserve_default=False,
        ),
    ]
