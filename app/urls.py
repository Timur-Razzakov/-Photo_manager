from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import PhotoListView, Logout, PhotoCreateView, PhotoUpdateView
from . import views

# router = DefaultRouter()
# # router.register(r'show all photo', PhotoShowViewSet)
# router.register(r'add new photo and meta data', PhotoViewSet)
# urlpatterns  = [
# path('', include(router.urls)),
# ]

# urlpatterns = format_suffix_patterns([
#     path('images/<int:pk>', PhotoRetrieveView.as_view()),
#     path('images/update/<int:pk>', PhotoUpdateView.as_view()),
#     path('images/all', PhotoListView.as_view()),
#     path('images/new', PhotoCreateView.as_view()),
# ])
urlpatterns = format_suffix_patterns([
    path('images/', views.PhotoViewSet.as_view({'get': 'list'})),
    path('images/<int:pk>/', views.PhotoViewSet.as_view({'get': 'retrieve'})),
    path("create/", views.PhotoCreateViewSet.as_view({'post': 'create'})),
    path("update/<int:pk>/", views.PhotoUpdateViewSet.as_view({'post': 'create'})),
])
# urlpatterns = [
#     path('images/', views.PhotoListView.as_view()),
#     path('images/<int:pk>/', views.PhotoDetailView.as_view()),
#     path("create/", views.PhotoCreateView.as_view()),
#
# ]
