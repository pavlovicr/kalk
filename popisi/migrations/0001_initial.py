# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 22:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaporedna_stevilka_del', models.IntegerField(null=True)),
                ('koda_del', models.CharField(max_length=50, null=True)),
                ('opis_del', models.CharField(max_length=50, verbose_name='Opis del')),
                ('splosna_dolocila_del', models.TextField(default='splošna določila za dela IZKOPI ', max_length=2000)),
            ],
            options={
                'ordering': ['zaporedna_stevilka_del'],
            },
        ),
        migrations.CreateModel(
            name='Objekt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv_objekta', models.CharField(max_length=50, null=True)),
                ('neto_povrsina_objekta', models.DecimalField(decimal_places=2, default='0.00', max_digits=20)),
                ('bruto_povrsina_objekta', models.DecimalField(decimal_places=2, default='0.00', max_digits=20)),
                ('opis_objekta', models.TextField(default='opis objekta ', max_length=2000)),
            ],
            options={
                'ordering': ['naziv_objekta'],
            },
        ),
        migrations.CreateModel(
            name='Podrocje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koda_podrocja', models.CharField(max_length=50, null=True)),
                ('naziv_podrocja', models.CharField(default='industrijski_objekti', max_length=50)),
                ('splosna_dolocila_podrocja', models.TextField(default='splošna določila področja industrijske gradnje', max_length=2000)),
            ],
            options={
                'ordering': ['koda_podrocja'],
            },
        ),
        migrations.CreateModel(
            name='Postavka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaporedna_stevilka_postavke', models.IntegerField(null=True)),
                ('koda_postavke', models.CharField(max_length=100, null=True)),
                ('opis_postavke', models.CharField(max_length=100)),
                ('enota_mere', models.CharField(max_length=10)),
                ('splosna_dolocila_postavke', models.TextField(default='splošna določila postavke', max_length=1000)),
                ('dela', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='popisi.Dela')),
            ],
            options={
                'ordering': ['zaporedna_stevilka_postavke'],
            },
        ),
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv_projekta', models.CharField(default='naziv projekta', max_length=200, null=True)),
                ('opis_projekta', models.TextField(default='opis projekta ', max_length=2000)),
                ('datum_projekta', models.DateField()),
                ('uporabnik', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-datum_projekta'],
            },
        ),
        migrations.CreateModel(
            name='Skupina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaporedna_stevilka_skupine', models.IntegerField(null=True)),
                ('koda_skupine', models.CharField(max_length=50, null=True)),
                ('naziv_skupine', models.CharField(default='Zemeljska dela', max_length=50, verbose_name='Naziv skupine')),
                ('splosna_dolocila_skupine', models.TextField(default='splošna določila skupine ZEMELJSKA DELA ', max_length=2000)),
            ],
            options={
                'ordering': ['zaporedna_stevilka_skupine'],
            },
        ),
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
        migrations.CreateModel(
            name='SpecifikacijaPostavke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaporedna_stevilka_specifikacije', models.IntegerField(null=True)),
                ('koda_specifikacije', models.CharField(max_length=50, null=True)),
                ('vsebina_specifikacije', models.CharField(max_length=100, verbose_name='standardna vsebina specifikacije postavke')),
                ('splosna_dolocila_specifikacije', models.TextField(default='splošna določila specifikacije', max_length=2000)),
                ('info', models.TextField(default='tehnične informacije', max_length=2000)),
            ],
            options={
                'ordering': ['zaporedna_stevilka_specifikacije'],
            },
        ),
        migrations.CreateModel(
            name='Zvrst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zaporedna_stevilka_zvrsti', models.IntegerField(null=True)),
                ('koda_zvrsti', models.CharField(max_length=50, null=True)),
                ('naziv_zvrsti', models.CharField(default='GRADBENA DELA', max_length=50, verbose_name='Naziv zvrsti')),
                ('splosna_dolocila_zvrsti', models.TextField(default='splošna določila zvrsti GRADBENA DELA ', max_length=2000)),
            ],
            options={
                'ordering': ['zaporedna_stevilka_zvrsti'],
            },
        ),
        migrations.AddField(
            model_name='skupina',
            name='zvrst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popisi.Zvrst'),
        ),
        migrations.AddField(
            model_name='postavka',
            name='specifikacija',
            field=models.ManyToManyField(to='popisi.SpecifikacijaPostavke'),
        ),
        migrations.AddField(
            model_name='objekt',
            name='podrocje',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='popisi.Podrocje'),
        ),
        migrations.AddField(
            model_name='objekt',
            name='projekt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popisi.Projekt'),
        ),
        migrations.AddField(
            model_name='dela',
            name='podrocje',
            field=models.ManyToManyField(default=[1, 2, 3, 4], to='popisi.Podrocje'),
        ),
        migrations.AddField(
            model_name='dela',
            name='skupina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='popisi.Skupina'),
        ),
    ]