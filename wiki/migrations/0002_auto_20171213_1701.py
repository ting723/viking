# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=200, verbose_name='comment content'),
        ),
    ]