from django.urls import path

from main.views.organization import (
    OrganizationReadView,
    OrganizationSwitchView,
    OrganizationUpdateView,
)
from main.views.organization.activities import OrganizationActivitiesListView
from main.views.user import (
    UserCreateView,
    UserReadView,
    UserSignInView,
    UserSignOutView,
    UserStartVerifyEmailView,
    UserUpdateView,
    UserVerifyEmailView,
)

urlpatterns = [
    path("organization/", OrganizationReadView.as_view()),
    path("organization/activities/", OrganizationActivitiesListView.as_view()),
    path("organization/switch/", OrganizationSwitchView.as_view()),
    path("organization/update/", OrganizationUpdateView.as_view()),
    path("user/", UserReadView.as_view()),
    path("user/create/", UserCreateView.as_view()),
    path("user/sign_in/", UserSignInView.as_view()),
    path("user/sign_out/", UserSignOutView.as_view()),
    path("user/start_verify_email/", UserStartVerifyEmailView.as_view()),
    path("user/update/", UserUpdateView.as_view()),
    path("user/verify_email/", UserVerifyEmailView.as_view()),
]
