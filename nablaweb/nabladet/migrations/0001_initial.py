# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nablad',
            fields=[
                ('news_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='news.News')),
                ('pub_date', models.DateField(help_text=b'Publikasjonsdato', null=True, verbose_name=b'publisert')),
                ('file', models.FileField(help_text=b'Filnavn', upload_to=b'nabladet', verbose_name=b'PDF-fil')),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name': 'nablad',
                'verbose_name_plural': 'nablad',
            },
            bases=('news.news',),
        ),
    ]
