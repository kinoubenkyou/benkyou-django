from django.urls import path

from main.views.organization.switch import OrganizationSwitchView

urlpatterns = [
    path("switch/", OrganizationSwitchView.as_view(), name="organization-switch"),
]
