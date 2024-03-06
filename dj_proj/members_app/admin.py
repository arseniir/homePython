from django.contrib import admin
from .models import UserEnrollment


class UserEnrollmentAdmin(admin.ModelAdmin):
    uselist_display = ('enrollment_date')
    

admin.site.register(UserEnrollment, UserEnrollmentAdmin)
