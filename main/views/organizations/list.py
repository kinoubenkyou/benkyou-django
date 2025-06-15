from django.contrib.auth.mixins import LoginRequiredMixin

from main.forms.organizations.list import OrganizationsListForm
from main.models import Organization
from main.views.list import ListView


class OrganizationsListView(LoginRequiredMixin, ListView):
    form_class = OrganizationsListForm
    model = Organization
    object_fields = ("code", "name")
