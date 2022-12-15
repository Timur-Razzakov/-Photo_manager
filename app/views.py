# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from .models import Photo
from .serializers import PhotoDetailSerializer, PhotoListSerializer


class PhotoViewSet(generics.ListAPIView):
    """Вывод списка изображений"""
    serializer_class = PhotoListSerializer
    queryset = Photo.objects.all()
    # filter_backends = [filters.SearchFilter]
    # filterset_fields = ['geo_position', 'created_at', 'names_people_photo']

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
