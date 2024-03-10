from django.urls import path
from .views import inputFormMembers, plusMinusWay


urlpatterns = [
    path('members/', inputFormMembers.as_view(), name='members'),
    path('random_page/', plusMinusWay, name='random_page'),
]

