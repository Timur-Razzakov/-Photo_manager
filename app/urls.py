from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# class MyCustomRouter(routers.DefaultRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'list'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'retrieve'})
#     ]
#
#
# router = MyCustomRouter()
# router.register(r'images', PhotoViewSet, basename='images')
# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = format_suffix_patterns([
    path('', views.PhotoViewSet.as_view()),
    path("image/create/", views.PhotoAPICreate.as_view()),
    path("image/<int:pk>/", views.PhotoAPIDeleteUpdate.as_view()),
])
