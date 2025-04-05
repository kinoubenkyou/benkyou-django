__all__ = [
    "UserCreateView",
    "UserDeleteView",
    "UserReadView",
    "UserSignInView",
    "UserSignOutView",
    "UserStartVerifyEmailView",
    "UserUpdateView",
]

from main.views.user.create import UserCreateView
from main.views.user.delete import UserDeleteView
from main.views.user.read import UserReadView
from main.views.user.sign_in import UserSignInView
from main.views.user.sign_out import UserSignOutView
from main.views.user.start_verify_email import UserStartVerifyEmailView
from main.views.user.update import UserUpdateView
