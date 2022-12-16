from rest_framework import serializers

from .models import Photo


class PhotoListSerializer(serializers.ModelSerializer):
    """Вывод списка изображений"""

    class Meta:
        model = Photo
        fields = ("id", "image")


class PhotoDetailSerializer(serializers.ModelSerializer):
    """Вывод полной информации об изображении"""
    '''Автоматически заполняем поле User, после входа пользователя'''
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Photo
        fields = "__all__"
