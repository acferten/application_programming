import django_filters
from django_filters import NumberFilter

from .models import AdvUser


class ArticleFilter(django_filters.FilterSet):

    from = NumberFilter(method='filter_from')

    class Meta:
        model = AdvUser
        fields = ['id', 'first_name', 'last_name']

    def filter_from(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
