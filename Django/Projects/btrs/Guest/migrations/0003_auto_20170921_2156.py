# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_auto_20170921_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='TellAFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('FName', models.CharField(max_length=255)),
                ('FEmail', models.CharField(max_length=255)),
                ('Comments', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Friend',
            },
        ),
        migrations.RenameModel(
            old_name='UserData',
            new_name='User',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]