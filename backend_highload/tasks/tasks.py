from celery import shared_task
from django.core.mail import send_mail
from .models import Email

@shared_task
def send_email_task(email_id):
    email = Email.objects.get(id=email_id)
    send_mail(
        email.subject,
        email.body,
        'from@example.com',
        [email.recipient],
    )
    return f'Email sent to {email.recipient}'
