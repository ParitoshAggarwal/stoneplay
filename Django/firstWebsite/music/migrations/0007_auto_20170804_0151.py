# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='song_file',
            field=models.FileField(default='settings.MEDIA_ROOT/default_song.mp3', upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default='settings.MEDIA_ROOT/default_album.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='songs',
            name='file_type',
            field=models.CharField(default='mp3', max_length=20),
        ),
    ]
