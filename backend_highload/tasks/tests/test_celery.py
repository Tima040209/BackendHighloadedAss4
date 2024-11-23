from django.test import TestCase
from django.core import mail
from tasks.tasks import send_email_task
from unittest.mock import patch

class CeleryTests(TestCase):

    @patch('tasks.tasks.send_mail')
    def test_send_email_task(self, mock_send_mail):
        """Тестируем задачу Celery по отправке email"""
        mock_send_mail.return_value = 1  # Возвращаем успешный результат

        # Запускаем асинхронную задачу
        send_email_task('test@example.com', 'Test Subject', 'Test Body')

        # Проверяем, что задача отправки письма была вызвана
        mock_send_mail.assert_called_with(
            'Test Subject',
            'Test Body',
            'from@example.com',
            ['test@example.com']
        )
