from django_filters import rest_framework as filters, DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    class F(FilterSet):
        date = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at']