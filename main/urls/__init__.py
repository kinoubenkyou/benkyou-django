from django.urls import path
from django.urls.conf import include

from main.urls import api, user

urlpatterns = [
    path("api/", include(api)),
    path("user/", include(user)),
]
