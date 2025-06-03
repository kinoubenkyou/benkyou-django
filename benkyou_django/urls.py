from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)

from main.routers.single_resource import SingleResourceRouter
from main.views.api.user.token import UserTokenApiView
from main.views.user.create import UserCreateView
from main.views.user.delete import UserDeleteView
from main.views.user.read import UserReadView
from main.views.user.sign_in import UserSignInView
from main.views.user.sign_out import UserSignOutView
from main.views.user.start_reset_password import UserStartResetPasswordView
from main.views.user.start_verify_email import UserStartVerifyEmailView
from main.views.user.update import UserUpdateView
from main.views.user.update_password import UserUpdatePasswordView
from main.views.user.verify_email import UserVerifyEmailView
from main.viewsets.user import UserViewSet

router = SingleResourceRouter()
router.register(r"user", UserViewSet, basename="api-user")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/user/token/", UserTokenApiView.as_view(), name="api-user-token"),
    path("user/", UserReadView.as_view(), name="user-read"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("user/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("user/sign_in/", UserSignInView.as_view(), name="user-sign-in"),
    path("user/sign_out/", UserSignOutView.as_view(), name="user-sign-out"),
    path(
        "user/start_reset_password/",
        UserStartResetPasswordView.as_view(),
        name="user-start-reset-password",
    ),
    path(
        "user/start_verify_email/",
        UserStartVerifyEmailView.as_view(),
        name="user-start-verify-email",
    ),
    path("user/update/", UserUpdateView.as_view(), name="user-update"),
    path(
        "user/update_password/",
        UserUpdatePasswordView.as_view(),
        name="user-update-password",
    ),
    path("user/verify_email/", UserVerifyEmailView.as_view(), name="user-verify-email"),
]

if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="api-schema"),
            name="api-schema-redoc",
        ),
    ]
