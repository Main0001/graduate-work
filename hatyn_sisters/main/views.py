from typing import Any, Dict
from django.shortcuts import render
import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from .models import Marker, ModelVillages, VillagesImageSet


class MarkersMapView(TemplateView):
    """Markers map view."""

    template_name = "main/map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", Marker.objects.all()))
        context["markers_obj"] = Marker.objects.exclude(village__name = 'Хатынь')
        return context


def index(request):
    context = {'title': 'Main page'}
    return render(request, 'main/main_page.html', context=context)

def bells(request):
    context = {'title': 'Bells information'}
    return render(request, 'main/bells-information.html', context=context)

def monument(request):
    context = {'title': 'Monument information'}
    return render(request, 'main/monument-information.html', context=context)


class VillagesListView(ListView):
    model = ModelVillages
    paginate_by = 1
    template_name = 'main/villages.html'  
    
    def get_context_data(self, *, object_list=None, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Villages'
        context['villages_obj'] = ModelVillages.objects.all()
        return context


def village_info(request, village_id):
    village_obj = ModelVillages.objects.filter(pk=village_id)
    img_set = VillagesImageSet.objects.filter(post=village_id)
    context = {'title': 'Village information', 'village': village_obj, 'img_set': img_set}
    return render(request, 'main/village-information.html', context=context)