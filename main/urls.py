from django.urls import path

from main.views import UserCreateView
from main.views import UserDetailView

urlpatterns = [
    path('users/<int:pk>/', UserDetailView.as_view(), name='user'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
]
