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


def forwards_func(apps, schema_editor):
    ContentType = apps.get_model("contenttypes", "ContentType")
    ct, _ = ContentType.objects.get_or_create(app_label="news", model="news")
    News = apps.get_model("news", "News")
    NewsArticle = apps.get_model("news", "NewsArticle")

    # db_alias = schema_editor.connection.alias
    ct_article, _ = ContentType.objects.get_or_create(app_label="news", model="newsarticle")
    news = News.objects.filter(content_type=ct)
    for n in news:
        a = NewsArticle()
        for field in fields_to_copy:
            setattr(a, field, getattr(n, field))
        a.id = n.id
        a.save()
        n.content_type = ct_article
        n.save(update_fields=["content_type"])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newsarticle'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
