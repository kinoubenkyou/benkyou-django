from django.views.generic import UpdateView

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
