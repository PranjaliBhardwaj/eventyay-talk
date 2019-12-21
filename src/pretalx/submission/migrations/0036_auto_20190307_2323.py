# Generated by Django 2.1.5 on 2019-03-07 23:23

from django.db import migrations


def remove_review_phases(apps, schema_editor):
    ReviewPhase = apps.get_model("submission", "ReviewPhase")
    ReviewPhase.objects.all().delete()


def create_review_phases(apps, schema_editor):
    import dateutil

    ReviewPhase = apps.get_model("submission", "ReviewPhase")
    Event = apps.get_model("event", "Event")
    EventSettings = apps.get_model("event", "Event_SettingsStore")

    for event in Event.objects.all():
        deadline = getattr(
            EventSettings.objects.filter(object=event, key="review_deadline").first(),
            "value",
            None,
        )
        hide_speakers = (
            getattr(
                EventSettings.objects.filter(
                    object=event, key="review_hide_speaker_names"
                ).first(),
                "value",
                "False",
            )
            == "True"
        )
        ReviewPhase.objects.create(
            event=event,
            name="Review",
            start=None,
            end=dateutil.parser.parse(deadline) if deadline else None,
            is_active=True,
            can_review=True,
            can_see_other_reviews="after_review",
            can_see_speaker_names=not hide_speakers,
            can_change_submission_state=False,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0035_reviewphase"),
    ]

    operations = [
        migrations.RunPython(create_review_phases, remove_review_phases),
    ]
