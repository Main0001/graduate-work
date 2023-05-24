from django import forms
from django.forms import inlineformset_factory
from .models import ModelEvents, EventsImageSet

from django.utils.translation import gettext_lazy as _

class EventForm(forms.ModelForm):
    class Meta:
        model = ModelEvents
        fields = ('name', 'description', 'date', 'video', 'village')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-add-name', 'placeholder': _('Enter event name')}),
            'description': forms.Textarea(),
            'date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-add-date', 'type': 'date'}),
            'video': forms.TextInput(attrs={'class': 'form-add-video'}),
            'village': forms.Select(attrs={'class': 'form-add-village'}),
        }
        labels = {
            'name': _('Event name'),
            'description': _('Event description'),
            'date': _('Event date'),
            'video': _('Youtube video url'),
            'village': _('The village where the event took place'),
        }

EventImageFormSet = inlineformset_factory(
    ModelEvents,
    EventsImageSet,
    fields=('image',),
    extra=1,
    can_delete=False,
    widgets={'image': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-add-images'})}
)