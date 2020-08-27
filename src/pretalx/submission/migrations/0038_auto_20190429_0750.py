# Generated by Django 2.2 on 2019-04-29 07:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0037_auto_20190404_2246"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submission",
            name="recording_source",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="recording_url",
        ),
        migrations.AlterField(
            model_name="track",
            name="color",
            field=models.CharField(
                max_length=7,
                validators=[
                    django.core.validators.RegexValidator("#([0-9A-Fa-f]{3}){1,2}")
                ],
            ),
        ),
    ]
