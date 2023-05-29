from modeltranslation.translator import register, TranslationOptions
from .models import ModelSights, ModelEvents, ModelSightsEventsCategories, Marker, ModelVillages

@register(ModelEvents)
class ModelEventsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(ModelSights)
class ModelSightsTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(ModelSightsEventsCategories)
class ModelSightsEventsCategoriesTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(Marker)
class MarkerTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(ModelVillages)
class ModelVillagesTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)