from django.db import models


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=254)
    subject = models.CharField(max_length=64)
    message = models.CharField(max_length=254)


class Rate(models.Model):
    type = models.CharField(max_length=5)  # noqa
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)


class Banks(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=255)
    email_from = models.CharField(max_length=60)
    number_phone = models.CharField(max_length=30)

    def __str__(self):
        return f"Bank object number: {self.id}"
