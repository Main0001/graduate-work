# Generated by Django 3.2 on 2023-05-16 09:26

import ckeditor_uploader.fields
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelSightsEventsCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='ModelVillages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='villages_media_covers/%Y/%m/%d/', verbose_name='Обложка')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelsightseventscategories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'деревня',
                'verbose_name_plural': 'деревни',
            },
        ),
        migrations.CreateModel(
            name='VillagesImageSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(default=1, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='villages_media_images/%Y/%m/%d/', verbose_name='Изображение')),
                ('content_type', models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.modelvillages', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Фото к деревне',
                'verbose_name_plural': 'Фото к деревням',
            },
        ),
        migrations.CreateModel(
            name='ModelSights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='Название')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sights_media_images/%Y/%m/%d/', verbose_name='Изображение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelsightseventscategories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'достопримечательность',
                'verbose_name_plural': 'достопримечательности',
            },
        ),
        migrations.CreateModel(
            name='ModelEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('date', models.DateField(verbose_name='Дата')),
                ('video', embed_video.fields.EmbedVideoField(verbose_name='Видео')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('sights', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelsights', verbose_name='Достопримечательность')),
            ],
            options={
                'verbose_name': 'событие',
                'verbose_name_plural': 'события',
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelvillages', verbose_name='Точки на карте')),
            ],
            options={
                'verbose_name': 'точка на карте',
                'verbose_name_plural': 'точки на карте',
            },
        ),
        migrations.CreateModel(
            name='EventsImageSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(default=1, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events_media_images/%Y/%m/%d/', verbose_name='Изображение')),
                ('content_type', models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.modelevents', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Фото к событию',
                'verbose_name_plural': 'Фото к событиям',
            },
        ),
    ]
