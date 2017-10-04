# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.CharField(choices=[('N', 'Nature'), ('C', 'City'), ('P', 'Portraits'), ('A', 'Animals')], default='', max_length=1),
        ),
    ]
