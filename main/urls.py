from django.urls import path

from main.views.user_views import UserCreateView, UserCreateDoneView

urlpatterns = [
    path("users/create/", UserCreateView.as_view()),
    path("users/create_done/", UserCreateDoneView.as_view()),
]
