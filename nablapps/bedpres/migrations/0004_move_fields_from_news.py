# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 01:04
from __future__ import unicode_literals
from django.db import migrations

fields_to_copy = [
    'body',
    'created_by',
    'created_date',
    'cropping',
    'headline',
    'last_changed_by',
    'last_changed_date',
    'lead_paragraph',
    'picture',
    'publication_date',
    'published',
    'slug',
    'view_counter',
]
app_label, model = "bedpres", "Bedpres"


def forwards_func(apps, schema_editor):
    DependentObject = apps.get_model(app_label, model)
    ContentType = apps.get_model("contenttypes", "ContentType")
    db_alias = schema_editor.connection.alias
    objects = DependentObject.objects.using(db_alias).all().select_related("news_ptr")
    for o in objects:
        news = o.news_ptr
        for field in fields_to_copy:
            setattr(o, field, getattr(news, field))
        o.save()
        news.content_type = ContentType.objects.get(app_label=app_label, model=model.lower())
        news.save(update_fields=["content_type"])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('bedpres', '0003_auto_20171006_1230'),
        ('news', '0005_auto_20171006_0216'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
