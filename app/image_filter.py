# from django_filters import rest_framework as filters
#
# from photo_manager.app.models import Photo
#
#
# class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
#     pass
#
#
# class ImageFilter(filters.FilterSet):
#     geo_position = CharFilterInFilter(field_name='photo__geo_position', lookup_expr='in')
#     names_people_photo = CharFilterInFilter(field_name='photo__names_people_photo', lookup_expr='in')
#     created_at = filters.RangeFilter()
#
#     class Meta:
#         model = Photo
#         fields = ['geo_position', 'created_at', 'names_people_photo']
