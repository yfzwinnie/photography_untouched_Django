# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_photo_sub_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='sub_category',
            new_name='city',
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
