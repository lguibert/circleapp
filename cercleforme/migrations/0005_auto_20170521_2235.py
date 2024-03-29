# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cercleforme', '0004_auto_20170521_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('zipcode', models.IntegerField()),
                ('city', models.CharField(default='Paris', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='address',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cercleforme.Address'),
            preserve_default=False,
        ),
    ]
