# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-15 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180415_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='attempt_type',
            field=models.CharField(choices=[('Practice', 'Practice'), ('Quiz', 'Quiz')], max_length=8),
        ),
    ]