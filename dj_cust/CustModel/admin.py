from django.contrib import admin
from .models import MyCustomUser

class MyCustomUserAdmin(admin.ModelAdmin):
    uselist_display = ('MyCustomUser')

admin.site.register(MyCustomUser, MyCustomUserAdmin)

