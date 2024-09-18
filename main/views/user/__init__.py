__all__ = [
    "UserCreateView",
    "UserReadView",
    "UserSignInView",
    "UserSignOutView",
    "UserStartVerifyEmailView",
    "UserVerifyEmailView",
]

from main.views.user.create import UserCreateView
from main.views.user.read import UserReadView
from main.views.user.sign_in import UserSignInView
from main.views.user.sign_out import UserSignOutView
from main.views.user.start_verify_email import UserStartVerifyEmailView
from main.views.user.verify_email import UserVerifyEmailView
