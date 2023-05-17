from django import forms
from django.forms import inlineformset_factory
from .models import ModelEvents, EventsImageSet

class EventForm(forms.ModelForm):
    class Meta:
        model = ModelEvents
        fields = ('name', 'description', 'date', 'video', 'village')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-add-name', 'placeholder': 'Введите название события'}),
            'description': forms.Textarea(),
            'date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-add-date', 'type': 'date'}),
            'video': forms.TextInput(attrs={'class': 'form-add-video'}),
            'village': forms.Select(attrs={'class': 'form-add-village'}),
        }
        labels = {
            'name': 'Название события',
            'description': 'Описание события',
            'date': 'Дата события',
            'video': 'Ссылка на видео с YouTube',
            'village': 'Деревня, в которой произошло событие',
        }

EventImageFormSet = inlineformset_factory(
    ModelEvents,
    EventsImageSet,
    fields=('image',),
    extra=1,
    can_delete=False,
    widgets={'image': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-add-images'})}
)