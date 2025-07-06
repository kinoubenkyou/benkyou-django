from django.urls import path

from main.views.organizations.read import OrganizationsReadView

urlpatterns = [
    path("<int:pk>/", OrganizationsReadView.as_view(), name="organizations-read"),
]
