from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    return 'uploads/avatars/{0}/{1}'.format(instance.id, filename)


class User(AbstractUser):
    avatar = models.FileField(null=True, blank=True, default=None, upload_to=user_directory_path)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        'email address', blank=False, null=False, unique=True,
    )
