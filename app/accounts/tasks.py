from celery import shared_task
from django.conf import settings

from django.core.mail import send_mail


@shared_task
def send_registration_email(body, email_to):
    title = 'Activate your account!'
    send_mail(
        title,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email_to],
        fail_silently=False,
    )
