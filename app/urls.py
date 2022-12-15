from django.urls import path
from . import views
from .views import PhotoViewSet

# class MyCustomRouter(routers.SimpleRouter):
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

urlpatterns = [
    path('images/', views.PhotoViewSet.as_view()),
    path("images/create/", views.PhotoAPICreate.as_view()),
    path("images/<int:pk>/", views.PhotoAPIDeleteUpdate.as_view()),
]
