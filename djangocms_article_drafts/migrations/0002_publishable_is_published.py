# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_article_drafts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishable',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
