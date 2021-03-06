# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-01 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('blood_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='signup',
            name='phone_num',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='patientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Signup'),
        ),
    ]
