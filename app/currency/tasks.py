from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email_contactus(body):
    send_mail(
        'Hello from contactus!',
        body,
        'PavelTest1990@gmail.com',
        ['zelenskiy.zelia@gmail.com'],
        fail_silently=False,
    )
