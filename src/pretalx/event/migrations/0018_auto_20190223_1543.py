# Generated by Django 2.1.5 on 2019-02-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0031_auto_20190223_0730"),
        ("event", "0017_auto_20180922_0511"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="limit_tracks",
            field=models.ManyToManyField(blank=True, to="submission.Track"),
        ),
        migrations.AlterField(
            model_name="event",
            name="timezone",
            field=models.CharField(default="UTC", max_length=30),
        ),
    ]
