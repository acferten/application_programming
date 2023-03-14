from django.urls import path

from .views import *

urlpatterns = [
    path('<pk>', AccountView.as_view(), name='detail'),
]
