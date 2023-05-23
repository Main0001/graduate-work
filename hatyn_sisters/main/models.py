from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from django.contrib.gis.db.models import PointField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField


class ModelSightsEventsCategories(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('name'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))

    class Meta:
        verbose_name = _('category')#'категорию'
        verbose_name_plural = _('categories')#'категории'

    def __str__(self):
        return f'{self.name}'


class ModelVillages(models.Model):
    name = models.CharField(max_length=127, verbose_name=_('name'))
    description = RichTextUploadingField(blank=True, null=True, verbose_name=_('description'))
    category = models.ForeignKey(to=ModelSightsEventsCategories, on_delete=models.CASCADE, verbose_name=_('category'))
    cover = models.ImageField(upload_to='villages_media_covers/%Y/%m/%d/', blank=True, null=True, verbose_name=_('cover'))
    stone_inscription = models.ImageField(upload_to='villages_media_stone_inscriptions/%Y/%m/%d/', blank=True, null=True, verbose_name=_('stone inscription'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('time create'))

    class Meta:
        verbose_name = _('village')#'деревня'
        verbose_name_plural = _('villages')#'деревни'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('main:village', kwargs={'village_id': self.pk})


class VillagesImageSet(models.Model):
    id = models.AutoField
    object_id = models.PositiveIntegerField(null=True, default=1)
    post = models.ForeignKey(to=ModelVillages, null=True, blank=True, verbose_name=_('post'), on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='villages_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name=_('image'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=20)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _('image for village')#'Фото к деревне'
        verbose_name_plural =_('images for village') #'Фото к деревням'


class ModelSights(models.Model):
    name = models.CharField(max_length=127, verbose_name=_('name'))
    description = RichTextUploadingField(blank=True, null=True, verbose_name=_('description'))
    image = models.ImageField(upload_to='sights_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name=_('image'))
    category = models.ForeignKey(to=ModelSightsEventsCategories, on_delete=models.CASCADE, verbose_name=_('category'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('time create'))

    class Meta:
        verbose_name = _('sight')#'достопримечательность'
        verbose_name_plural = _('sights')#'достопримечательности'

    def __str__(self):
        return f'{self.name}'


class ModelEvents(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('name'))
    description = RichTextUploadingField(blank=True, null=True, verbose_name=_('description'))
    date = models.DateField(verbose_name=_('date'))
    video = EmbedVideoField(blank=True, null=True, verbose_name=_('youtube video url'))
    village = models.ForeignKey(to=ModelVillages, on_delete=models.CASCADE, verbose_name=_('village'))
    time_create = models.DateTimeField(auto_now_add=True, verbose_name=_('time create'))
    draft = models.BooleanField(default=True, verbose_name=_('draft'))
    

    class Meta:
        verbose_name = _('event name')#'событие'
        verbose_name_plural = _('events name')#'события'

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('main:event', kwargs={'event_id': self.pk})


class EventsImageSet(models.Model):
    id = models.AutoField(primary_key=True)
    object_id = models.PositiveIntegerField()
    post = models.ForeignKey(to=ModelEvents, null=True, blank=True, verbose_name=_('post'), on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='events_media_images/%Y/%m/%d/', blank=True, null=True, verbose_name=_('image'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _('image for event')#'Фото к событию'
        verbose_name_plural = _('images for event')#'Фото к событиям'


class Marker(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = RichTextUploadingField(verbose_name=_('description'))
    village = models.ForeignKey(to=ModelVillages, on_delete=models.CASCADE, verbose_name=_('point on map'))
    location = PointField()

    class Meta:
        verbose_name = _('point on map')#'точка на карте'
        verbose_name_plural = _('points on map')#'точки на карте'

    def __str__(self):
        return f'{self.name}: {self.location}'