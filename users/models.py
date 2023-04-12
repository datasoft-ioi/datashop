from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    phone = models.CharField(max_length=23, blank=True, null=True)
    is_verified_email = models.BooleanField(default=False)

    
class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self) -> str:
        return f"EmailVerification object for {self.user.email}"

    
    def send_verification_email(self):
        send_mail(
            'Sunbjdect here',
            'heje is message mess',
            'from@gmail.com',
            [self.user.email],
            fail_silently=False,
        )
