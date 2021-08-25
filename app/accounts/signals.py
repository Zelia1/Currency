from accounts.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    if instance.USERNAME_FIELD == 'email':
        instance.email = instance.email.lower()
    # or
    # if instance.email:
    #     instance.email = instance.email.lower()

