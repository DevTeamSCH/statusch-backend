# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_room', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machine',
            old_name='type',
            new_name='kind_of',
        ),
    ]