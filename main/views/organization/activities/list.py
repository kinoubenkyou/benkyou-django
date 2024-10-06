from main.documents.organization_activity import OrganizationActivity
from main.forms.organization.activities import OrganizationActivitiesListForm
from main.views.activities_list import ActivitiesListView
from main.views.mixin import OrganizationRequiredMixin


class OrganizationActivitiesListView(OrganizationRequiredMixin, ActivitiesListView):
    form_class = OrganizationActivitiesListForm
    queryset = OrganizationActivity.objects.all()
    template_name = "main/organization/activities/list.html"

    def get_queryset(self):
        return super().get_queryset().filter(object_id=self.request.organization.id)
