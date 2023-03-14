from django.urls import path

from .views import *

urlpatterns = [
    path('<pk>', AnimalDetailView.as_view(), name='detail'),
]
