from django.urls import path

from .views import *

urlpatterns = [
    path('search', SearchAccountView.as_view(), name='account-search'),
    path('<pk>', AccountView.as_view(), name='account-detail'),
]
