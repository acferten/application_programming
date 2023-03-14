from django.urls import path

from .views import *

urlpatterns = [
    path('search', SearchAccountView.as_view(), name='detail'),
    path('<pk>', AccountView.as_view(), name='detail'),
]
