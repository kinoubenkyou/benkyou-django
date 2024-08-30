from django.urls import path

from main.views import SignInView, SignInDoneView
from main.views.user_views import UserCreateView, UserCreateDoneView

urlpatterns = [
    path("sign_in/", SignInView.as_view()),
    path("sign_in/done/", SignInDoneView.as_view()),
    path("users/create/", UserCreateView.as_view()),
    path("users/create_done/", UserCreateDoneView.as_view()),
]
