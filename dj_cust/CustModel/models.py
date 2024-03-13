from django.db import models
from django.contrib.auth.models import AbstractUser

class MyCustomUser(AbstractUser):
    phone = models.CharField(max_length=10, unique=True)
    