from django.shortcuts import get_object_or_404
from icecream import ic
from rest_framework import generics, permissions
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Photo
from .serializers import PhotoDetailSerializer, PhotoListSerializer
from rest_framework.exceptions import PermissionDenied


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка изображений"""
    queryset = Photo.objects.all()
    """Переопределяем метод  """

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        elif self.action == "retrieve":
            return PhotoDetailSerializer


class PhotoAPICreate(generics.CreateAPIView):
    """Добавление новых изображений"""
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PhotoAPIDeleteUpdate(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление и удаление существующий изображений"""
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
