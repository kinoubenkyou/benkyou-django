from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)

from main.routers import SingleResourceRouter
from main.views.api.user import UserTokenApiView
from main.views.user import (
    UserCreateView,
    UserDeleteView,
    UserReadView,
    UserSignInView,
    UserSignOutView,
    UserUpdateView,
)
from main.viewsets import UserViewSet

router = SingleResourceRouter()
router.register(r"user", UserViewSet, basename="api-user")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/user/token/", UserTokenApiView.as_view(), name="api-user-token"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("user/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("user/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/", UserReadView.as_view(), name="user-read"),
    path("user/sign_in/", UserSignInView.as_view(), name="user-sign-in"),
    path("user/sign_out/", UserSignOutView.as_view(), name="user-sign-out"),
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
