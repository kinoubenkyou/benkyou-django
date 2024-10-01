from django.views.generic import ListView

from main.documents.organization_activity import OrganizationActivity
from main.forms.organization.activities import OrganizationActivityListForm
from main.models import User
from main.views.mixin import OrganizationRequiredMixin


class OrganizationActivitiesListView(OrganizationRequiredMixin, ListView):
    form = None
    queryset = OrganizationActivity.objects.all()
    template_name = "main/organization/activities/list.html"

    def get(self, request, *args, **kwargs):
        self.form = OrganizationActivityListForm(data=self.request.GET)
        self.form.is_valid()
        return super().get(request, *args, **kwargs)

    def get_ordering(self):
        return self.form.cleaned_data["sort_by"] or self.ordering

    def get_queryset(self):
        return (
            super().get_queryset().filter(object_id=self.request.organization.id)
            if self.form.is_valid()
            else self.queryset.none()
        )

    def get_context_data(self, **kwargs):
        return_ = super().get_context_data(form=self.form, **kwargs)
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
