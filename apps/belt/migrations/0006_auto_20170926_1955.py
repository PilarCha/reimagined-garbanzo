# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0005_auto_20170926_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='favorite_Quote',
        ),
        migrations.AddField(
            model_name='quote',
            name='favorite',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_by', to='belt.User'),
            preserve_default=False,
        ),
    ]
