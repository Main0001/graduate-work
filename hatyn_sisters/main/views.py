from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
import json

from django.utils.translation import gettext_lazy as _

from django.http import Http404
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.contenttypes.models import ContentType

from .models import Marker, ModelVillages, VillagesImageSet, ModelSights, ModelEvents, EventsImageSet
from .forms import EventForm, EventImageFormSet


class MarkersMapView(TemplateView):
    template_name = 'main/map.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Map')
        context['markers'] = json.loads(serialize('geojson', Marker.objects.all()))
        context['markers_obj'] = Marker.objects.exclude(village__name = 'Хатынь')
        return context


class IndexView(TemplateView):
    template_name = 'main/main-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Main page')
        context['villages_obj'] = ModelVillages.objects.all()[:6]
        context['villages_obj_inscriptions'] = ModelVillages.objects.exclude(stone_inscription = "")[:12]
        return context
    

class BellsView(TemplateView):
    template_name = 'main/bells-information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Bells information')
        context['bells_obj'] = ModelSights.objects.filter(name='Колокола Хатыни')
        return context
    

class MonumentView(TemplateView):
    template_name= 'main/monument-information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Monument information')
        context['monument_obj'] = ModelSights.objects.filter(name='Памятник "Непокоренный"')
        return context


class VillagesListView(ListView):
    model = ModelVillages
    paginate_by = 8
    context_object_name = 'villages_obj'
    template_name = 'main/villages.html'  
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = _('Villages')
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = ModelVillages.objects.exclude(cover='')
        return queryset


class VillageInfoView(DetailView):
    model = ModelVillages
    template_name = 'main/village-information.html'
    pk_url_kwarg = 'village_id'
    context_object_name = 'village_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Village information')
        context['img_set'] = VillagesImageSet.objects.filter(post=self.get_object().id)
        return context


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        formset = EventImageFormSet(request.POST, request.FILES, prefix='eventsimageset_set')
        
        if form.is_valid() and formset.is_valid():
            event = form.save()
            
            for i, form in enumerate(formset.forms):
                if form.is_valid() and f'eventsimageset_set-{i}-image' in request.FILES:
                    image = request.FILES.getlist(f'eventsimageset_set-{i}-image')[:6]
                    for img in image:
                        instance = EventsImageSet(post=event, image=img, content_type=ContentType.objects.get_for_model(ModelEvents), object_id=event.id)
                        instance.save()
            return redirect('main:index')
            
    else:
        form = EventForm()
        formset = EventImageFormSet(prefix='eventsimageset_set')
    
    context = {
        'form': form,
        'formset': formset,
        'title': _('Create event')
    }
    return render(request, 'main/create-event.html', context)


class EventsListView(ListView):
    model = ModelVillages
    paginate_by = 12
    context_object_name = 'villages_obj'
    template_name = 'main/events.html'    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = _('Events')
        context['events_obj'] = ModelEvents.objects.filter(draft=False)
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = ModelVillages.objects.filter(draft=False)
        return queryset


class EventInfoView(DetailView):
    model = ModelEvents
    template_name = 'main/event-information.html'
    pk_url_kwarg = 'event_id'
    context_object_name = 'event_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Event information')
        context['img_set'] = EventsImageSet.objects.filter(post=self.get_object().id)
        return context
    
    def get_object(self, queryset=None):
        event = super().get_object(queryset=queryset)
        if event.draft:
            raise Http404("Event not found.")
        return event