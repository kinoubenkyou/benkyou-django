from django.urls import path

from main.views import UserCreateView
from main.views import UserDetailView

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
]
