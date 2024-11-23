from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient

class SecurityTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client = APIClient()

    def test_csrf_protection(self):
        """Тестируем защиту от CSRF атак"""
        url = reverse('send_email')
        data = {
            'recipient': 'tima7087@gmail.com',
            'subject': 'Test Subject',
            'body': 'Test Body'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_rate_limiting(self):
        """Тестируем ограничение количества запросов (Rate Limiting)"""
        url = reverse('send_email')
        data = {
            'recipient': 'tima7087@gmail.com',
            'subject': 'Test Subject',
            'body': 'Test Body'
        }
        for _ in range(6):
            response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
