from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.

class AuthUser(models.Model):
    """ Модель пользователя
    """
    user_name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str___(self):
        return self.user_name


class Photo(models.Model):
    """модель для фотографий"""
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
