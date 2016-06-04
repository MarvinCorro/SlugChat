# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 21:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='fileRef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commenting.File'),
        ),
    ]
