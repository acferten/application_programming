from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>', AnimalDetailView.as_view(), name='detail'),
]
