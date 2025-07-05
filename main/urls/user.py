from django.urls import path

from main.views.user.create import UserCreateView
from main.views.user.delete import UserDeleteView
from main.views.user.read import UserReadView
from main.views.user.reset_password import UserResetPasswordView
from main.views.user.sign_in import UserSignInView
from main.views.user.sign_out import UserSignOutView
from main.views.user.start_reset_password import UserStartResetPasswordView
from main.views.user.start_verify_email import UserStartVerifyEmailView
from main.views.user.update import UserUpdateView
from main.views.user.update_password import UserUpdatePasswordView
from main.views.user.verify_email import UserVerifyEmailView

urlpatterns = [
    path("", UserReadView.as_view(), name="user-read"),
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("delete/", UserDeleteView.as_view(), name="user-delete"),
    path(
        "reset_password",
        UserResetPasswordView.as_view(),
        name="user-reset-password",
    ),
    path("sign_in/", UserSignInView.as_view(), name="user-sign-in"),
    path("sign_out/", UserSignOutView.as_view(), name="user-sign-out"),
    path(
        "start_reset_password/",
        UserStartResetPasswordView.as_view(),
        name="user-start-reset-password",
    ),
    path(
        "start_verify_email/",
        UserStartVerifyEmailView.as_view(),
        name="user-start-verify-email",
    ),
    path("update/", UserUpdateView.as_view(), name="user-update"),
    path(
        "update_password/",
        UserUpdatePasswordView.as_view(),
        name="user-update-password",
    ),
    path("verify_email/", UserVerifyEmailView.as_view(), name="user-verify-email"),
]
