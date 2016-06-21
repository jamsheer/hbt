# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('entry_date', models.DateTimeField(verbose_name='date added')),
            ],
        ),
    ]