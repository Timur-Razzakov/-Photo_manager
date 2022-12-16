from django_filters import rest_framework as rest_filters
from rest_framework import generics, permissions, filters

from .image_filter import ImageFilter
from .models import Photo
from .serializers import PhotoDetailSerializer, PhotoListSerializer


class PhotoViewSet(generics.ListAPIView):
    """Вывод списка изображений"""
    serializer_class = PhotoListSerializer
    queryset = Photo.objects.all()
    filter_backends = (rest_filters.DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['^names_people_photo', ]
    filterset_class = ImageFilter

    """Переопределяем метод  """
    #
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return PhotoListSerializer
    #     elif self.action == "retrieve":
    #         return PhotoDetailSerializer


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

# class PhotoViewSet(viewsets.ModelViewSet):
#     """ CRUD, изображений"""
#     queryset = Photo.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     """Переопределяем метод, если это просмотр всех изображений, то выводим только фото """
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return PhotoListSerializer
#         elif self.action == "retrieve":
#             return PhotoDetailSerializer
