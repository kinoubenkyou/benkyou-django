from django.urls import path
from django.urls.conf import include

from main.urls import api, organization, organizations, user

urlpatterns = [
    path("api/", include(api)),
    path("organization/", include(organization)),
    path("organizations/", include(organizations)),
    path("user/", include(user)),
]
