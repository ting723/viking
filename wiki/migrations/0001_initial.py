# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-13 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='blog id')),
                ('title', models.CharField(max_length=100, verbose_name='blog title')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='blog subtitle')),
                ('content', models.CharField(max_length=2000, verbose_name='blog content')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='blog created')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='comment id')),
                ('content', models.CharField(max_length=2000, verbose_name='comment content')),
                ('vote', models.IntegerField(choices=[(0, 'not vote score=0'), (1, 'zan vote score=1'), (-1, 'cai vote score=-1')], default=0, verbose_name='vote score')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='blog created')),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.Blog', verbose_name='Blog')),
            ],
        ),
    ]