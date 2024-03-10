from django.db import models
from django.contrib.auth.models import User
from members_app.models import UserEnrollment


class Courses(models.Model):
    course_name = models.CharField(max_length=88)
    enrollments = models.ManyToManyField(UserEnrollment, related_name='courses')