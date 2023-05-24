# Generated by Django 3.2.4 on 2023-05-23 11:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_modelvillages_stone_inscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='marker',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='marker',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='marker',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='modelevents',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelevents',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelevents',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='modelevents',
            name='name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='modelsights',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelsights',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelsights',
            name='name_en',
            field=models.CharField(max_length=127, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='modelsights',
            name='name_ru',
            field=models.CharField(max_length=127, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='modelsightseventscategories',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelsightseventscategories',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelsightseventscategories',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='modelsightseventscategories',
            name='name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='modelvillages',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelvillages',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='modelvillages',
            name='name_en',
            field=models.CharField(max_length=127, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='modelvillages',
            name='name_ru',
            field=models.CharField(max_length=127, null=True, verbose_name='Название'),
        ),
    ]