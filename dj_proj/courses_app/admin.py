from django.contrib import admin
from .models import Courses

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name',)


admin.site.register(Courses, CoursesAdmin)
