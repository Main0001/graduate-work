from django.contrib import admin
import django.contrib.gis.admin as OSMGadmin
from django.contrib.admin import TabularInline

from embed_video.admin import AdminVideoMixin

from .models import ModelSights, ModelEvents, ModelSightsEventsCategories, Marker, ModelVillages, VillagesImageSet, EventsImageSet #, EventsVideoSet


class Villages_imagesetInline(TabularInline):
    model = VillagesImageSet
    readonly_fields = ["object_id"]


class Events_imagesetInline(TabularInline):
    model = EventsImageSet
    readonly_fields = ["object_id"]


# class Events_videosetInline(TabularInline):
#     model = EventsVideoSet
#     readonly_fields = ["object_id"]


@admin.register(ModelVillages)
class VillagesAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    inlines = [Villages_imagesetInline]

    class Meta:
        model = ModelVillages


@admin.register(ModelSights)
class SightsAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = ModelSights


@admin.register(ModelEvents)
class EventsAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ["name", "date","description"]
    inlines = [Events_imagesetInline] #, Events_videosetInline]

    class Meta:
        model = ModelEvents


@admin.register(ModelSightsEventsCategories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

    class Meta:
        model = ModelSightsEventsCategories


@admin.register(Marker)
class MarkerAdmin(OSMGadmin.OSMGeoAdmin):
    list_display = ["name", "location"]

    class Meta:
        model = Marker