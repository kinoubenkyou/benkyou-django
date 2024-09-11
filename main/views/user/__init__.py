__all__ = [
    "UserCreateDoneView",
    "UserCreateView",
    "UserReadView",
    "UserSignInDoneView",
    "UserSignInView",
    "UserSignOutDoneView",
    "UserSignOutView",
    "UserStartVerifyEmailDoneView",
    "UserStartVerifyEmailView",
    "UserSwitchOrganizationDoneView",
    "UserSwitchOrganizationView",
    "UserVerifyEmailView",
]

from main.views.user.create import UserCreateView
from main.views.user.create_done import UserCreateDoneView
from main.views.user.read import UserReadView
from main.views.user.sign_in import UserSignInView
from main.views.user.sign_in_done import UserSignInDoneView
from main.views.user.sign_out import UserSignOutView
from main.views.user.sign_out_done import UserSignOutDoneView
from main.views.user.start_verify_email import UserStartVerifyEmailView
from main.views.user.start_verify_email_done import UserStartVerifyEmailDoneView
from main.views.user.switch_organization import UserSwitchOrganizationView
from main.views.user.switch_organization_done import UserSwitchOrganizationDoneView
from main.views.user.verify_email import UserVerifyEmailView
