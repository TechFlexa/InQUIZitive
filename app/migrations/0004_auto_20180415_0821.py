# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-15 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180415_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='attempt_type',
            field=models.IntegerField(choices=[('0', 'Practice'), ('1', 'Quiz')]),
        ),
    ]