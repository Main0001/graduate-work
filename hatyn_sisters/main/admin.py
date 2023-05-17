from django.contrib import admin
import django.contrib.gis.admin as OSMGadmin
from django.contrib.admin import TabularInline

from embed_video.admin import AdminVideoMixin

from .models import ModelSights, ModelEvents, ModelSightsEventsCategories, Marker, ModelVillages, VillagesImageSet, EventsImageSet


class Villages_imagesetInline(TabularInline):
    model = VillagesImageSet
    readonly_fields = ['object_id']


class Events_imagesetInline(TabularInline):
    model = EventsImageSet
    readonly_fields = ['object_id']

@admin.register(ModelVillages)
class VillagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    inlines = [Villages_imagesetInline]

    class Meta:
        model = ModelVillages


@admin.register(ModelSights)
class SightsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

    class Meta:
        model = ModelSights


@admin.register(ModelEvents)
class EventsAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'date', 'draft']
    search_fields = ['name']
    inlines = [Events_imagesetInline]

    class Meta:
        model = ModelEvents


@admin.register(ModelSightsEventsCategories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

    class Meta:
        model = ModelSightsEventsCategories


@admin.register(Marker)
class MarkerAdmin(OSMGadmin.OSMGeoAdmin):
    list_display = ['name', 'location']
    search_fields = ['name']

    class Meta:
        model = Marker