from django.contrib import admin
from django.urls import path
from django.urls.conf import include

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

router = SingleResourceRouter()  # type: ignore[no-untyped-call]
router.register(r"user/", UserViewSet, basename="api-user")  # type: ignore[no-untyped-call]


api_urlpatterns = [
    path("user/token/", UserTokenApiView.as_view(), name="api-user-token"),  # type: ignore[no-untyped-call]
    path("", include(router.urls)),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("user/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("user/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/", UserReadView.as_view(), name="user-read"),
    path("user/sign_in/", UserSignInView.as_view(), name="user-sign-in"),
    path("user/sign_out/", UserSignOutView.as_view(), name="user-sign-out"),
]
