from django.contrib import admin
from .models import ModelSights, ModelEvents, ModelSightsEventsCategories, ModelSightsImage, ModelEventsImage 

# Register your models here.
#admin.site.register(Categories)


@admin.register(ModelSightsEventsCategories)
class CategoriesAdmin(admin.ModelAdmin):
    pass

@admin.register(ModelSights)
class ModelSightsAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelEvents)
class ModelEventsAdmin(admin.ModelAdmin):
    pass


#class SightsImageInline(admin.StackedInline):
#    model = ModelSightsImage
#    max_num = 10
#    extra = 0


#class EventsImageInline(admin.StackedInline):
#    model = ModelEventsImage
#    max_num = 10
#    extra = 0

#admin.site.register(Sights, SightsAdmin)
#admin.site.register(Events, EventsAdmin)
