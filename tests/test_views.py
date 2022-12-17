from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class CaseTests(APITestCase):
    def setUp(self):
        # создаю несколько пользователей
        user_test_01 = User.objects.create(username="user_test20", password="4525testtest")
        user_test_01.save()
        user_test_02 = User.objects.create(username="user_test21", password="4525testtest")
        user_test_02.save()

        # данные модели Photo
        self.data = {'descriptions': 'hello world',
                     'names_people_photo': 'Александр, Вика',
                     'title': 'test-01',
                     'geo_position': 'USA',
                     'user_id': '1'
                     }
        # создаю токен для тестового пользователя
        self.user_test_01_token = Token.objects.create(user=user_test_01)
        self.user_test_02_token = Token.objects.create(user=user_test_02)

    def test_see_images_without_auth(self):
        """Проверяем можем ли мы просмотреть изображения без аутентификации """
        response = self.client.get('http://0.0.0.0:8000/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_invalid_image(self):
        """Проверяем можем ли мы создать изображения без аутентификации """
        response = self.client.get('http://0.0.0.0:8000/image/create/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


    def test_create_valid_image(self):
        """Проверяем можем ли мы создать изображения после аутентификации """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test_01_token.key)
        response = self.client.post('http://0.0.0.0:8000/image/create/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

