# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opman', '0011_auto_20160622_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xlsx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('filename', models.FileField(upload_to='./upload/xlsx/')),
            ],
        ),
    ]