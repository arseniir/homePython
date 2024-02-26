from django.urls import path
from .views import input_page_view, plusMinusWay


urlpatterns = [
    path('members/', input_page_view, name='members'),
    path('random_page/', plusMinusWay, name='random_page')
]

