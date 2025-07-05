from django.urls import path
from django.urls.conf import include

from main.urls import api, organizations, user

urlpatterns = [
    path("api/", include(api)),
    path("organizations/", include(organizations)),
    path("user/", include(user)),
]
