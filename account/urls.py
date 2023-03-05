from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>', AccountView.as_view(), name='detail'),
]
