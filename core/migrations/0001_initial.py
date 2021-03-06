# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Immobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Price')),
                ('objective', models.CharField(choices=[('for_sale', 'For Sale'), ('for_rent', 'For Rent')], max_length=30, verbose_name='Objective')),
                ('property_type', models.CharField(max_length=255, verbose_name='Property Type')),
                ('bedroms', models.PositiveSmallIntegerField(default=0, verbose_name='Bedrooms')),
                ('bathroms', models.PositiveSmallIntegerField(default=0, verbose_name='Bathrooms')),
                ('parking', models.PositiveSmallIntegerField(default=0, verbose_name='Parking')),
                ('city', models.CharField(max_length=75, verbose_name='City')),
                ('state', models.CharField(max_length=2, verbose_name='State')),
                ('neighborhood', models.CharField(blank=True, max_length=75, verbose_name='Neighborhood')),
                ('street', models.CharField(blank=True, max_length=75, verbose_name='Street')),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Immobile',
                'verbose_name_plural': 'Immobiles',
            },
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('name', models.CharField(max_length=140, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Real estate',
                'verbose_name_plural': 'Real estates',
            },
        ),
        migrations.AddField(
            model_name='immobile',
            name='realestate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.RealEstate'),
        ),
        migrations.AddField(
            model_name='image',
            name='immobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Immobile'),
        ),
    ]
