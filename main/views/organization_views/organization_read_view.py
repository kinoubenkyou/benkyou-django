from django.views.generic import TemplateView

from main.views import OrganizationRequiredMixin


class OrganizationReadView(OrganizationRequiredMixin, TemplateView):
    template_name = "main/organization/read.html"
