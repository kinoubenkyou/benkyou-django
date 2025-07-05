from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from main.routers.single_resource import SingleResourceRouter
from main.views.api.user.token import UserTokenApiView
from main.viewsets.user import UserViewSet

router = SingleResourceRouter()
router.register(r"user", UserViewSet, basename="api-user")

urlpatterns = [
    path("", include(router.urls)),
    path("user/token/", UserTokenApiView.as_view(), name="api-user-token"),
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
