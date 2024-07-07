from django.urls import path

from main.views import UserCreateView

urlpatterns = [
    path("user/add/", UserCreateView.as_view()),
]
