from django.urls import path

from main.views.user_views import (
    UserCreateView,
    UserCreateDoneView,
    UserSignInView,
    UserSignInDoneView,
)

urlpatterns = [
    path("user/sign_in/", UserSignInView.as_view()),
    path("user/sign_in/done/", UserSignInDoneView.as_view()),
    path("user/create/", UserCreateView.as_view()),
    path("user/create_done/", UserCreateDoneView.as_view()),
]
