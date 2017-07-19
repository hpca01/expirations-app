# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expirations', '0004_auto_20170630_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barCode', models.CharField(max_length=40)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barcode_for_drug', to='expirations.Drug')),
            ],
        ),
    ]