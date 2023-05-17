from django.urls import path

from .views import IndexView, BellsView, MonumentView, VillagesListView, MarkersMapView, VillageInfoView, events, create_event, EventInfoView

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('bells/', BellsView.as_view(), name='bells'),
    path("map/", MarkersMapView.as_view(), name='map'),
    path('monument/', MonumentView.as_view(), name='monument'),
    path('villages/', VillagesListView.as_view(), name='villages'),
    path('page/<int:page>/', VillagesListView.as_view(), name='paginator'),
    path('villages/<int:village_id>/', VillageInfoView.as_view(), name='village'),
    path('events/', events, name='events'),
    path('events/<int:event_id>/', EventInfoView.as_view(), name='event'),
    path('create-event/', create_event, name='create_event'),
]
