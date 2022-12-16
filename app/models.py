from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Photo(models.Model):
    """модель для фотографий"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    title = models.CharField(max_length=120, verbose_name='наименование фото')
    geo_position = models.CharField(max_length=400, verbose_name='геопозиция', blank=True, null=True, )
    descriptions = models.TextField(verbose_name='описание', blank=True, null=True, )
    names_people_photo = models.CharField(max_length=255, verbose_name='Имена людей на фото', blank=True,
                                          null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="photos",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
