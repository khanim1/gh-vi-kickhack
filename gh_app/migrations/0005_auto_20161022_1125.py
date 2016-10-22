# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gh_app', '0004_auto_20161022_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='last_shelter_visited',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shelters_visited', to='gh_app.Shelter'),
        ),
        migrations.AddField(
            model_name='person',
            name='shelters_visited',
            field=models.ManyToManyField(to='gh_app.Shelter'),
        ),
    ]