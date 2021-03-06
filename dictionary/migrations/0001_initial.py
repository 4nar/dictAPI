# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('definition', models.TextField()),
                ('language', models.CharField(choices=[('en', 'english'), ('ru', 'russian'), ('kz', 'kazakh')], max_length=3)),
                ('antonyms', models.ManyToManyField(related_name='_word_antonyms_+', to='dictionary.Word')),
                ('synonyms', models.ManyToManyField(related_name='_word_synonyms_+', to='dictionary.Word')),
                ('translation', models.ManyToManyField(related_name='_word_translation_+', to='dictionary.Word')),
            ],
        ),
    ]
