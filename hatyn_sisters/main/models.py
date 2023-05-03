from django.db import models
from django.urls import reverse

from django.contrib.gis.db.models import PointField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ModelSightsEventsCategories(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'Категория: "{self.name}"'


class ModelVillages(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey(to=ModelSightsEventsCategories, on_delete=models.CASCADE, verbose_name='Категория')
    cover = models.ImageField(upload_to='villages_media_covers/%Y/%m/%d/', blank=True, null=True, verbose_name='Обложка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'деревня'
        verbose_name_plural = 'деревни'

    def __str__(self):
        return f'Деревня: "{self.name}"'

    def get_absolute_url(self):
        return f'{self.pk}/'


class VillagesImageSet(models.Model):
    id = models.AutoField
    object_id = models.PositiveIntegerField(null=True, default=1)
    post = models.ForeignKey(to=ModelVillages, null=True, blank=True, verbose_name="Статья", on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='villages_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=20)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = 'Фото к деревне'
        verbose_name_plural = 'Фото к деревням'


class ModelSights(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='sights_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(to=ModelSightsEventsCategories, on_delete=models.CASCADE, verbose_name='Категория')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'достопримечательность'
        verbose_name_plural = 'достопримечательности'

    def __str__(self):
        return f'Достопримечательнсть: "{self.name}"'


class ModelEvents(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    sights = models.ForeignKey(to=ModelSights, on_delete=models.CASCADE, verbose_name='Достопримечательность')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'

    def __str__(self):
        return f'Событие: "{self.name}"'


class EventsImageSet(models.Model):
    id = models.AutoField
    object_id = models.PositiveIntegerField(null=True, default=1)
    post = models.ForeignKey(to=ModelEvents, null=True, blank=True, verbose_name="Статья", on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='events_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=20)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = 'Фото к событию'
        verbose_name_plural = 'Фото к событиям'


class EventsVideoSet(models.Model):
    id = models.AutoField
    object_id = models.PositiveIntegerField(null=True)
    post = models.ForeignKey(to=ModelEvents, null=True, blank=True, verbose_name="Статья", on_delete=models.SET_NULL)
    video = models.FileField(upload_to='events_media_videos/%Y/%m/%d/', blank=True, null=True, verbose_name='Видео')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=20)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = 'Видео к статье'
        verbose_name_plural = 'Видео к статьям'


class Marker(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextUploadingField()
    village = models.ForeignKey(to=ModelVillages, on_delete=models.CASCADE, verbose_name='Точки на карте')
    location = PointField()

    class Meta:
        verbose_name = 'точка на карте'
        verbose_name_plural = 'точки на карте'

    def __str__(self):
        return f'Координаты точки {self.name}: "{self.location}"'