from django.views.generic import ListView

from main.documents.organization_activity import OrganizationActivity
from main.models import User
from main.views.mixin import OrganizationRequiredMixin


class OrganizationActivitiesListView(OrganizationRequiredMixin, ListView):
    ordering = ["object_id", "-timestamp"]
    paginate_by = 10
    template_name = "main/organization/activities/list.html"

    def get_queryset(self):
        return OrganizationActivity.objects.filter(
            object_id=self.request.organization.id,
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        return_ = super().get_context_data(object_list=object_list, **kwargs)
        return_["object_list"] = list(return_["object_list"])
        users = {
            user.id: user
            for user in User.objects.filter(
                id__in=[object_.user_id for object_ in return_["object_list"]],
            )
        }
        for object_ in return_["object_list"]:
            object_.user = users.get(object_.user_id)
        return return_
