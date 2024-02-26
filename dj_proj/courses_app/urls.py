from django.urls import path
from .views import courses_send


urlpatterns = [
    path('courses/', courses_send, name='courses'),
]


