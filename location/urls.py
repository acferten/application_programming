from django.urls import path

from location.views import LocationDetailView

urlpatterns = [
    path('<pk>', LocationDetailView.as_view(), name='detail'),
]
