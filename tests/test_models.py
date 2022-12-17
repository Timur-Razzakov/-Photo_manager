from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase

from app.models import Photo


class TestModel(APITestCase):
    def test_registration(self):
        """Создаём пользователей """
        body = {"username": "user_test", "password": "4525testtest"}
        response = self.client.post("http://0.0.0.0:8000/auth/users/", body, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, 'user_test')
        self.assertEqual(User.objects.count(), 1)
        # сохраняем id, для модели Photo
        self.user_id = User.objects.get().id

    def test_model_photo(self):
        """Тестируем модель Photo"""
        self.test_registration()
        image = Photo.objects.create(descriptions='hello world', names_people_photo='Александр, Вика',
                                     title='test', geo_position='USA', user_id=self.user_id,
                                     image=None,
                                     )
        self.assertIsInstance(image, Photo)
        self.assertEqual(image.title, 'test')
