from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    email_confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = '1. User'