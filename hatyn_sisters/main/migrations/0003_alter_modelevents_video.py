# Generated by Django 3.2 on 2023-05-16 09:54

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_modelevents_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelevents',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Видео'),
        ),
    ]
