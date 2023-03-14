from django.contrib import admin
from django.urls import path, include

from account.views import CreateAccountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration', CreateAccountView.as_view(), name='signup'),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('account.urls')),
    path('animals/', include('animal.urls')),
    path('locations/', include('location.urls')),
]
