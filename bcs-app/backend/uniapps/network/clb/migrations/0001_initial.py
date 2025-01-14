# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-12-03 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CloudLoadBlancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=32, verbose_name='创建者')),
                ('updator', models.CharField(max_length=32, verbose_name='修改着')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_time', models.DateTimeField(blank=True, null=True)),
                ('clb_name', models.CharField(max_length=253)),
                ('resource_name', models.CharField(max_length=253)),
                ('project_id', models.CharField(max_length=32)),
                ('cluster_id', models.CharField(max_length=32)),
                ('namespace', models.CharField(default='bcs-system', max_length=253)),
                ('region', models.CharField(max_length=32)),
                ('image', models.CharField(max_length=512)),
                ('config', models.TextField()),
                ('vpc_id', models.CharField(max_length=32)),
                ('status', models.CharField(default='not_created', max_length=32)),
            ],
            options={'db_table': 'cloud_load_blancer',},
        ),
        migrations.AlterUniqueTogether(
            name='cloudloadblancer', unique_together=set([('clb_name', 'cluster_id', 'namespace')]),
        ),
    ]
