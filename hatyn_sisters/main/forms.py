from django import forms
from django.forms import inlineformset_factory
from .models import ModelEvents, EventsImageSet, ModelVillages

class EventForm(forms.ModelForm):
    class Meta:
        model = ModelEvents
        fields = ('name', 'description', 'date', 'video', 'village')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-add-name'}),
            'description': forms.Textarea(attrs={'class': 'form-add-description'}),
            'date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-add-date', 'placeholder': 'Выберите дату', 'type': 'date'}),
            'video': forms.TextInput(attrs={'class': 'form-add-video'}),
            'village': forms.Select(attrs={'class': 'form-add-village'}),

        }

EventImageFormSet = inlineformset_factory(
    ModelEvents,
    EventsImageSet,
    fields=('image',),
    extra=1,
    widgets={'image': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-add-images'})}
)