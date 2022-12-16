from django_filters import rest_framework as filters

from .models import Photo


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ImageFilter(filters.FilterSet):
    geo_position = CharFilterInFilter(field_name='geo_position', lookup_expr='in')
    user_created = CharFilterInFilter(field_name='user__username', lookup_expr='in')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Photo
        fields = ['geo_position', 'created_at','names_people_photo']
