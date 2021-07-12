from currency import choices

from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=64)
    message = models.CharField(max_length=254)
    created = models.DateTimeField(auto_now_add=True, null=True)


class Rate(models.Model):

    type = models.PositiveSmallIntegerField(choices=choices.RATE_TYPE_CHOICES) # noqa
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)


class Banks(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=255)
    email_from = models.CharField(max_length=60)
    number_phone = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Bank object number: {self.id}"


class Analytics(models.Model):
    path = models.CharField(max_length=255)
    status_code = models.CharField(max_length=3)
    create = models.DateTimeField(auto_now_add=True, null=True)
