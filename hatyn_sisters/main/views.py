from django.shortcuts import render
import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Marker, ModelVillages, VillagesImageSet, ModelSights


class MarkersMapView(TemplateView):
    template_name = 'main/map.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markers'] = json.loads(serialize('geojson', Marker.objects.all()))
        context['markers_obj'] = Marker.objects.exclude(village__name = 'Хатынь')
        return context


class IndexView(TemplateView):
    template_name = 'main/main-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['villages_obj'] = ModelVillages.objects.all()[:6]
        return context
    

class BellsView(TemplateView):
    template_name = 'main/bells-information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bells information'
        context['bells_obj'] = ModelSights.objects.filter(name='Колокола Хатыни')
        return context
    

class MonumentView(TemplateView):
    template_name= 'main/monument-information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Monument information'
        context['monument_obj'] = ModelSights.objects.filter(name='Колокола Хатыни')
        return context


def events(request):
    context = {'title': 'Events'} 
    return render(request, 'main/events.html', context=context)


class VillagesListView(ListView):
    model = ModelVillages
    paginate_by = 6
    context_object_name = 'villages_obj'
    template_name = 'main/villages.html'  
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Villages'
        return context


class VillageInfoView(DetailView):
    model = ModelVillages
    template_name = 'main/village-information.html'
    pk_url_kwarg = 'village_id'
    context_object_name = 'village_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Village information'
        context['img_set'] = VillagesImageSet.objects.filter(post=self.get_object().id)
        return context