# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("submission", "0006_auto_20170913_1142"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submission",
            name="accept_feedback",
        ),
        migrations.AlterField(
            model_name="cfp",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="cfp",
            name="default_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="submission.SubmissionType",
            ),
        ),
        migrations.AlterField(
            model_name="cfp",
            name="headline",
            field=i18nfield.fields.I18nCharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="cfp",
            name="text",
            field=i18nfield.fields.I18nTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="review",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="question",
            name="default_answer",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="position",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="question",
            name="question",
            field=i18nfield.fields.I18nCharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="question",
            name="required",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="submission",
            name="duration",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="submission",
            name="state",
            field=models.CharField(default="submitted", max_length=9),
        ),
        migrations.AlterField(
            model_name="submissiontype",
            name="default_duration",
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name="submissiontype",
            name="max_duration",
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AlterField(
            model_name="submissiontype",
            name="name",
            field=i18nfield.fields.I18nCharField(max_length=100),
        ),
    ]
