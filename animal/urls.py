from django.urls import path, include

from .views import *

urlpatterns = [
    path('<pk>', AnimalDetailView.as_view(), name='animal-detail'),
    path('types/<pk>', TypeDetailView.as_view(), name='animal-type'),
    path('<pk>/locations', include('location.urls'))
]
