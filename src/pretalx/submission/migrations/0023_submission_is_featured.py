# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0022_submission_review_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]
