# Generated by Django 2.1.5 on 2019-03-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20190311_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='F.eks. sommerjobb, bergen, kirkenes, olje, konsultering...', to='jobs.TagChoices', verbose_name='Tags'),
        ),
    ]
