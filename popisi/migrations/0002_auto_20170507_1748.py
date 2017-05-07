# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('popisi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specifikacijapostavke',
            name='postavka',
        ),
        migrations.AddField(
            model_name='postavka',
            name='specifikacija',
            field=models.ManyToManyField(to='popisi.SpecifikacijaPostavke'),
        ),
        migrations.AlterField(
            model_name='dela',
            name='podrocje',
            field=models.ManyToManyField(default=[1, 2, 3], to='popisi.Podrocje'),
        ),
        migrations.AlterField(
            model_name='popis',
            name='objekt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='popisi.Objekt'),
        ),
    ]