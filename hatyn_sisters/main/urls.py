from django.urls import path

from .views import index, bells, monument, villages

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('bells/', bells, name='bells'),
    path('monument/', monument, name='monument'),
    path('villages/', villages, name='villages')
]
