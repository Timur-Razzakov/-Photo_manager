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


# class PhotoListView(APIView):
#     """Вывод списка изображений"""
#
#     def get(self, request):
#         images = Photo.objects.all()
#         serializer = PhotoListSerializer(images, many=True)
#         return Response(serializer.data)
#
#
# class PhotoDetailView(APIView):
#     """Вывод подробной информации об изображении"""
#
#     def get(self, request, pk):
#         image = Photo.objects.get(id=pk)
#         serializer = PhotoDetailSerializer(image)
#         return Response(serializer.data)
#
# class PhotoCreateView(APIView):
#     """Добавление изображений и мета данных"""
#     def post(self, request):
#         review = PhotoDetailView(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)
#
#
# class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вывод списка изображений"""
#     queryset = Photo.objects.all()
#     serializer_class = PhotoListSerializer
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return PhotoListSerializer
#         elif self.action == "retrieve":
#             return PhotoCreateSerializer
#
#
#
# class PhotoCreateViewSet(viewsets.ModelViewSet):
#     """Добавление новых изображений"""
#     serializer_class = PhotoCreateSerializer
#     # permission_class = permissions.IsAuthenticatedOrReadOnly
#
#
# class PhotoUpdateViewSet(viewsets.ModelViewSet):
#     """Обновление существующий изображений"""
#     queryset = Photo.objects.all()
#     serializer_class = PhotoCreateSerializer
#     # permission_class = permissions.IsAuthenticatedOrReadOnly
# #
#
#
#
#
#
#
#
#


# class IsUser(permissions.BasePermission):
#     """Проверяем есть ли доступ у пользователя"""
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user
#

# class Logout(APIView):
#     def get(self, request):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

# class PhotoRetrieveView(generics.RetrieveAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoCreateSerializer
#     # permission_class = permissions.IsAuthenticatedOrReadOnly
#
#
# class PhotoUpdateView(generics.UpdateAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoCreateSerializer
#     # permission_classes = (IsUser,)
#
#
# class PhotoCreateView(generics.CreateAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoCreateSerializer
#
#
# class PhotoListView(generics.ListAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка изображений"""
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        elif self.action == "retrieve":
            return PhotoDetailSerializer


class PhotoCreateViewSet(viewsets.ModelViewSet):
    """Добавление новых изображений"""
    serializer_class = PhotoDetailSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class PhotoUpdateViewSet(viewsets.ModelViewSet):
    """Обновление существующий изображений"""
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly



#
# @action(methods=['get'], detail=True)
# def get_message(self, request, pk=None):
#     """ Получаем сообщения, которые привязаны к указанной рассылке и выводим их"""
#     photos = Photo.objects.all()
#     get_object_or_404(photo_manager, pk=pk)
#     get_message = Message.objects.filter(mailing_id=pk).all()
#     serializer = MessageSerializer(get_message, many=True)
#     return Response(serializer.data)
#
# @action(methods=['get'], detail=False)
# def get_total_info(self, request):
#     """
#     Выводим полную информацию о сообщениях для рассылок
#     """
#     total_mailings = Mailing.objects.count()
#     mailing = Mailing.objects.values('pk')
#     content = {'The number of photo_manager': total_mailings,
#                'The number of messages and their status': ''}
#     result = {}
#     # для каждой рассылке выводим общую статистику
#     for item in mailing:
#         ic(item)
#         static = {'Total messages': 0, 'Sent': 0, 'No sent': 0}
#         all_messages = Message.objects.filter(mailing_id=item['pk']).all()
#         group_sent = all_messages.filter(sending_status='True').count()
#         group_no_sent = all_messages.filter(sending_status='False').count()
#         static['Total messages'] = len(all_messages)
#         static['Sent'] = group_sent
#         static['No sent'] = group_no_sent
#         result[item['pk']] = static
#
#     content['The number of messages and their status'] = result
#     return Response(content)
