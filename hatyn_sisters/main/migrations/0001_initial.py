# Generated by Django 3.2.4 on 2023-05-29 10:32

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
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('name_ru', models.CharField(max_length=128, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=128, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ModelVillages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='name')),
                ('name_ru', models.CharField(max_length=127, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=127, null=True, verbose_name='name')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='villages_media_covers/%Y/%m/%d/', verbose_name='cover')),
                ('stone_inscription', models.ImageField(blank=True, null=True, upload_to='villages_media_stone_inscriptions/%Y/%m/%d/', verbose_name='stone inscription')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='time create')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelsightseventscategories', verbose_name='category')),
            ],
            options={
                'verbose_name': 'village',
                'verbose_name_plural': 'villages',
            },
        ),
        migrations.CreateModel(
            name='VillagesImageSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(default=1, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='villages_media_images/%Y/%m/%d/', verbose_name='image')),
                ('content_type', models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.modelvillages', verbose_name='post')),
            ],
            options={
                'verbose_name': 'image for village',
                'verbose_name_plural': 'images for village',
            },
        ),
        migrations.CreateModel(
            name='ModelSights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='name')),
                ('name_ru', models.CharField(max_length=127, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=127, null=True, verbose_name='name')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sights_media_images/%Y/%m/%d/', verbose_name='image')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='time create')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelsightseventscategories', verbose_name='category')),
            ],
            options={
                'verbose_name': 'sight',
                'verbose_name_plural': 'sights',
            },
        ),
        migrations.CreateModel(
            name='ModelEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('name_ru', models.CharField(max_length=128, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=128, null=True, verbose_name='name')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description')),
                ('date', models.DateField(verbose_name='date')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='youtube video url')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='time create')),
                ('draft', models.BooleanField(default=True, verbose_name='draft')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelvillages', verbose_name='village')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='name')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelvillages', verbose_name='point on map')),
            ],
            options={
                'verbose_name': 'point on map',
                'verbose_name_plural': 'points on map',
            },
        ),
        migrations.CreateModel(
            name='EventsImageSet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField(default=1, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events_media_images/%Y/%m/%d/', verbose_name='image')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.modelevents', verbose_name='post')),
            ],
            options={
                'verbose_name': 'image for event',
                'verbose_name_plural': 'images for event',
            },
        ),
    ]
