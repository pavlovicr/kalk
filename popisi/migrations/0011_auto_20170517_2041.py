# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popisi', '0010_postavka_specifikacija'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkupinaSpecifikacije',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaporedna_stevilka_skupine_specifikacije', models.IntegerField(null=True)),
                ('koda_skupine_specifikacije', models.CharField(max_length=50, null=True)),
                ('opis_skupine_specifikacije', models.CharField(max_length=50, verbose_name='Opis skupine specifikacije')),
                ('splosna_dolocila_skupine_specifikacije', models.TextField(default='splošna določila za skupino specifikacije npr. kategorije zemljišča ', max_length=2000)),
                ('dela', models.ManyToManyField(to='popisi.Dela')),
            ],
            options={
                'ordering': ['zaporedna_stevilka_skupine_specifikacije'],
            },
        ),
        migrations.RemoveField(
            model_name='specifikacijapostavke',
            name='dela',
        ),
    ]
