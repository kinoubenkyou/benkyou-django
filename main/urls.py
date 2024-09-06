from django.urls import path

from main.views.organization_views import OrganizationReadView
from main.views.user_views import (
    UserCreateDoneView,
    UserCreateView,
    UserReadView,
    UserSignInDoneView,
    UserSignInView,
    UserVerifyEmailView,
    UserSwitchOrganizationView,
    UserSwitchOrganizationDoneView,
    UserStartVerifyEmailView,
    UserStartVerifyEmailDoneView,
)

urlpatterns = [
    path("organization/", OrganizationReadView.as_view()),
    path("user/create/", UserCreateView.as_view()),
    path("user/create_done/", UserCreateDoneView.as_view()),
    path("user/", UserReadView.as_view()),
    path("user/sign_in/", UserSignInView.as_view()),
    path("user/sign_in/done/", UserSignInDoneView.as_view()),
    path("user/start_verify_email/", UserStartVerifyEmailView.as_view()),
    path("user/start_verify_email/done/", UserStartVerifyEmailDoneView.as_view()),
    path("user/switch_organization/", UserSwitchOrganizationView.as_view()),
    path("user/switch_organization/done/", UserSwitchOrganizationDoneView.as_view()),
    path("user/verify_email/", UserVerifyEmailView.as_view()),
]
