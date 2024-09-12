from django.views.generic import DetailView

from main.views.mixin.organization_required import OrganizationRequiredMixin


class OrganizationReadView(OrganizationRequiredMixin, DetailView):
    template_name = "main/organization/read.html"

    def get_object(self, _queryset=None):
        return self.request.organization
