# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-03 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='channel',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]