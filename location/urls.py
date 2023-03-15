from django.urls import path

from .views import *

urlpatterns = [
    path('', AnimalLocationsView.as_view(), name='animal-locations'),
    path('<pk>', LocationDetailView.as_view(), name='location-detail'),
]
