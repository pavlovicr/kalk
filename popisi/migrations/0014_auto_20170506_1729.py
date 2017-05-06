# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popisi', '0013_delpostavke_dela'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delpostavke',
            name='dela',
        ),
        migrations.AddField(
            model_name='delpostavke',
            name='postavka',
            field=models.ManyToManyField(to='popisi.Postavka'),
        ),
    ]