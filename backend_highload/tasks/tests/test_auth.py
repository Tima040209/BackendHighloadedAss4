from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

class AuthenticationTests(TestCase):

    def setUp(self):
        # Создаем пользователя для тестирования
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_register_user(self):
        """Тестируем регистрацию пользователя"""
        url = reverse('user_register')  # Убедитесь, что у вас есть URL для регистрации
        data = {
            'username': 'newuser',
            'password': 'newpassword123',
            'password_confirm': 'newpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        """Тестируем вход пользователя"""
        url = reverse('user_login')  # Убедитесь, что у вас есть URL для входа
        data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login_invalid_password(self):
        """Тестируем вход с неверным паролем"""
        url = reverse('user_login')
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
