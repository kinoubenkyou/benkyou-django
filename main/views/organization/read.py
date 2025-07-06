from main.models import Organization
from main.views.organization.object_mixin import OrganizationObjectMixin
from main.views.read import ReadView


class OrganizationReadView(OrganizationObjectMixin, ReadView):
    model = Organization
    object_fields = ("code", "name")
