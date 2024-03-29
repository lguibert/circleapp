# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('day', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=150)),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cercleforme.Room'),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cercleforme.CourseTypes'),
        ),
    ]
