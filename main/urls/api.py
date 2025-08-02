from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from main.routers.single_resource import SingleResourceRouter
from main.viewsets.organizations import OrganizationsViewSet
from main.viewsets.user import UserViewSet

simple_router = SimpleRouter()
simple_router.register(
    r"organizations", OrganizationsViewSet, basename="api-organizations"
)
single_resource_router = SingleResourceRouter()
single_resource_router.register(r"user", UserViewSet, basename="api-user")

urlpatterns = [
    path("", include(single_resource_router.urls)),
    path("", include(simple_router.urls)),
    path("blacklist_token/", TokenBlacklistView.as_view(), name="api-blacklist-token"),
    path(
        "obtain_token_pair/",
        TokenObtainPairView.as_view(),
        name="api-obtain-token-pair",
    ),
    path("refresh_token/", TokenRefreshView.as_view(), name="api-refresh-token"),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns.extend(
        (
            path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
            path(
                "schema/redoc/",
                SpectacularRedocView.as_view(url_name="api-schema"),
                name="api-schema-redoc",
            ),
        )
    )
