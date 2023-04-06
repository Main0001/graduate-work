from django.db import models
from django.utils import timezone

# Create your models here.
class SightsCategories(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'Категория {self.name}'


class Sights(models.Model):
    name = models.CharField(max_length=127, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    images = models.ImageField(upload_to='sights_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')
    video = models.FileField(upload_to='sights_media_videos/%Y/%m/%d/', blank=True, null=True, verbose_name='Видео')
    category = models.ForeignKey(to=SightsCategories, on_delete=models.CASCADE, verbose_name='Категория')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'достопримечательность'
        verbose_name_plural = 'достопримечательности'

    def __str__(self):
        return f'Достопримечательнсть {self.name} категории {self.category}'


class Events(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    date = models.DateField(verbose_name='Дата')
    images = models.ImageField(upload_to='events_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')
    video = models.FileField(upload_to='events_media_videos/%Y/%m/%d/', blank=True, null=True, verbose_name='Видео')
    sights = models.ForeignKey(to=Sights, on_delete=models.CASCADE, verbose_name='Достопримечательность')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'

    def __str__(self):
        return f'Событие {self.name} достопримечтаельности {self.sights}'

