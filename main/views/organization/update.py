from django.views.generic import UpdateView

from main.documents import OrganizationActivity
from main.forms.organization import OrganizationUpdateForm
from main.models import Organization
from main.views.mixin import OrganizationRequiredMixin


class OrganizationUpdateView(OrganizationRequiredMixin, UpdateView):
    form_class = OrganizationUpdateForm
    model = Organization
    success_url = "/organization/"
    template_name = "main/organization/update.html"

    def get_object(self, _queryset=None):
        return self.request.organization

    def form_valid(self, form):
        return_ = super().form_valid(form)
        OrganizationActivity.objects.create(
            object_id=form.instance.id,
            user_id=self.request.user.id,
            action=OrganizationActivity.UPDATE_ACTION,
            data={key: form.cleaned_data[key] for key in ("code", "name")},
        )
        return return_
