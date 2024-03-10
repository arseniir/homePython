from django.db import models
from django.contrib.auth.models import User


class UserEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)
