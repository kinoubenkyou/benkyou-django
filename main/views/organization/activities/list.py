from django.views.generic import ListView

from main.documents.organization_activity import OrganizationActivity
from main.views.mixin import OrganizationRequiredMixin


class OrganizationActivitiesListView(OrganizationRequiredMixin, ListView):
    template_name = "main/organization/activities/list.html"

    def get_queryset(self):
        return OrganizationActivity.objects.filter(
            object_id=self.request.organization.id,
        )
