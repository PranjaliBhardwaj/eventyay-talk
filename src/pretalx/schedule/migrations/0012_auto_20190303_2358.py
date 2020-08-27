# Generated by Django 2.1.5 on 2019-03-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0011_auto_20180205_1127"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talkslot",
            name="is_visible",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name="talkslot",
            unique_together=set(),
        ),
    ]
