# Generated by Django 2.0.3 on 2018-05-30 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0015_remove_event_subtitle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="permitted",
        ),
    ]
