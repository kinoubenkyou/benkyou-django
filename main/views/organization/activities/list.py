from django.views.generic import TemplateView

from main.documents.organization_activity import OrganizationActivity
from main.models import User
from main.views.mixin import OrganizationRequiredMixin


class OrganizationActivitiesListView(OrganizationRequiredMixin, TemplateView):
    template_name = "main/organization/activities/list.html"

    def get_context_data(self, **kwargs):
        return_ = super().get_context_data(**kwargs)
        activities = list(
            OrganizationActivity.objects.filter(
                object_id=self.request.organization.id,
            ),
        )
        users = {
            user.id: user
            for user in User.objects.filter(
                id__in=[activity.user_id for activity in activities],
            )
        }
        for activity in activities:
            activity.user_email = users[activity.user_id]
        return_.update(activities=activities)
        return return_
