# Generated by Django 2.0.8 on 2018-09-22 10:11

from django.db import migrations, models
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0016_remove_event_permitted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="landing_page_text",
            field=i18nfield.fields.I18nTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="locale",
            field=models.CharField(default="en", max_length=32),
        ),
        migrations.AlterField(
            model_name="team",
            name="review_override_votes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
