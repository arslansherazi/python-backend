# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_auto_20170921_2156'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TellAFriend',
            new_name='Friend',
        ),
        migrations.AlterModelTable(
            name='friend',
            table=None,
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]