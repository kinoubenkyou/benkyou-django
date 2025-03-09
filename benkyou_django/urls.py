"""
URL configuration for benkyou_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

from main.routers import SingleResourceRouter
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
    path("user/get_token/", obtain_auth_token, name="api-user-get-token"),
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
