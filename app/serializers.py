from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Photo


class PhotoListSerializer(serializers.ModelSerializer):
    """Вывод списка изображений"""
    '''Автоматически заполняем поле User, после входа пользователя'''
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Photo
        fields = ("id", "image")


class PhotoDetailSerializer(serializers.ModelSerializer):
    """Вывод полной информации об изображении"""

    class Meta:
        model = Photo
        fields = "__all__"
