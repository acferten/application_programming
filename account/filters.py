import django_filters
from django_filters import NumberFilter

from .models import AdvUser


class AccountFilter(django_filters.FilterSet):
    class Meta:
        model = AdvUser
        fields = '__all__'

