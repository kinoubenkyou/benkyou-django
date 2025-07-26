from django.urls import path

from main.views.organization.read import OrganizationReadView
from main.views.organization.switch import OrganizationSwitchView

urlpatterns = [
    path("", OrganizationReadView.as_view(), name="organization-read"),
    path("switch/", OrganizationSwitchView.as_view(), name="organization-switch"),
]
