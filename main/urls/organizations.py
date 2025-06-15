from django.urls import path

from main.views.organizations.list import OrganizationsListView
from main.views.organizations.read import OrganizationsReadView

urlpatterns = [
    path("", OrganizationsListView.as_view(), name="organizations-list"),
    path("<int:pk>/", OrganizationsReadView.as_view(), name="organizations-read"),
]
