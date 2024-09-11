from django.urls import path

from main.views.organization import OrganizationReadView, OrganizationUpdateView
from main.views.organization.activities import OrganizationActivitiesListView
from main.views.user import (
    UserCreateDoneView,
    UserCreateView,
    UserReadView,
    UserSignInDoneView,
    UserSignInView,
    UserSignOutDoneView,
    UserSignOutView,
    UserStartVerifyEmailDoneView,
    UserStartVerifyEmailView,
    UserSwitchOrganizationDoneView,
    UserSwitchOrganizationView,
    UserVerifyEmailView,
)

urlpatterns = [
    path("organization/", OrganizationReadView.as_view()),
    path("organization/activities/", OrganizationActivitiesListView.as_view()),
    path("organization/update/", OrganizationUpdateView.as_view()),
    path("user/", UserReadView.as_view()),
    path("user/create/", UserCreateView.as_view()),
    path("user/create_done/", UserCreateDoneView.as_view()),
    path("user/sign_in/", UserSignInView.as_view()),
    path("user/sign_in/done/", UserSignInDoneView.as_view()),
    path("user/sign_out/", UserSignOutView.as_view()),
    path("user/sign_out/done/", UserSignOutDoneView.as_view()),
    path("user/start_verify_email/", UserStartVerifyEmailView.as_view()),
    path("user/start_verify_email/done/", UserStartVerifyEmailDoneView.as_view()),
    path("user/switch_organization/", UserSwitchOrganizationView.as_view()),
    path("user/switch_organization/done/", UserSwitchOrganizationDoneView.as_view()),
    path("user/verify_email/", UserVerifyEmailView.as_view()),
]
