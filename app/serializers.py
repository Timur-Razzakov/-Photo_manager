from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AuthUser, Photo


class PhotoListSerializer(serializers.ModelSerializer):
    """Вывод списка изображений"""

    class Meta:
        model = Photo
        fields = ("id", "image")


class PhotoDetailSerializer(serializers.ModelSerializer):
    """Вывод полной информации об изображении"""

    class Meta:
        model = Photo
        fields = "__all__"
