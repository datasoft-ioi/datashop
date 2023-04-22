import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    phone = models.CharField(max_length=23, blank=True, null=True)

    # adress dastavki


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=113)
    otp = models.CharField(max_length=123, null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4)
    
    USERNAME_FIELD = 'user'

    def __str__(self) -> str:
        return self.user.username
    
    