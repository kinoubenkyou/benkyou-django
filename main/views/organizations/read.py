from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import Organization
from main.views.read import ReadView


class OrganizationsReadView(LoginRequiredMixin, ReadView):
    model = Organization
    object_fields = ("code", "name")
