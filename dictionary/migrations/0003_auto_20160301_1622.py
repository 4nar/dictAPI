# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_auto_20160301_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='antonyms',
            field=models.ManyToManyField(blank=True, related_name='_word_antonyms_+', to='dictionary.Word'),
        ),
        migrations.AddField(
            model_name='word',
            name='synonyms',
            field=models.ManyToManyField(blank=True, related_name='_word_synonyms_+', to='dictionary.Word'),
        ),
        migrations.AlterField(
            model_name='word',
            name='translation',
            field=models.ManyToManyField(blank=True, related_name='_word_translation_+', to='dictionary.Word'),
        ),
    ]
