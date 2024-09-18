__all__ = [
    "UserChangePasswordView",
    "UserCreateView",
    "UserReadView",
    "UserSignInView",
    "UserSignOutView",
    "UserStartVerifyEmailView",
    "UserUpdateView",
    "UserVerifyEmailView",
]

from main.views.user.change_password import UserChangePasswordView
from main.views.user.create import UserCreateView
from main.views.user.read import UserReadView
from main.views.user.sign_in import UserSignInView
from main.views.user.sign_out import UserSignOutView
from main.views.user.start_verify_email import UserStartVerifyEmailView
from main.views.user.update import UserUpdateView
from main.views.user.verify_email import UserVerifyEmailView
