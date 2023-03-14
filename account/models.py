from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
