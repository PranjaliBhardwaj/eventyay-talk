# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0005_schedule_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="talkslot",
            name="is_visible",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
