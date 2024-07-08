from django.urls import path

from main.views import UserCreateView

urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
]
