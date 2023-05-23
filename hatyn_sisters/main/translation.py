from modeltranslation.translator import register, TranslationOptions
from .models import ModelSights, ModelEvents, ModelSightsEventsCategories, Marker, ModelVillages

@register(ModelEvents)
class ModelEventsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(ModelSights)
class ModelEventsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(ModelSightsEventsCategories)
class ModelEventsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(Marker)
class ModelEventsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(ModelVillages)
class ModelEventsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)