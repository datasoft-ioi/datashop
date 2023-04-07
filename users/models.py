from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    phone = models.CharField(max_length=23, blank=True, null=True)

    # adress dastavki

    