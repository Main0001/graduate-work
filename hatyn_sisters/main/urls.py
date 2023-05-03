from django.urls import path

from .views import index, bells, monument, VillagesListView, MarkersMapView, village_info

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('bells/', bells, name='bells'),
    path('monument/', monument, name='monument'),
    path('villages/', VillagesListView.as_view(), name='villages'),
    path('page/<int:page>', VillagesListView.as_view(), name='paginator'),
    path('villages/<int:village_id>/', village_info, name='village'),
    path("map/", MarkersMapView.as_view(), name='map'),
]
