from django.contrib import admin
from .models import Sights, Events, SightsCategories

# Register your models here.
admin.site.register(Sights)
admin.site.register(Events)
admin.site.register(SightsCategories)

