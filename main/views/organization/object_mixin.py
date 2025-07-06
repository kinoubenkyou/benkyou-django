from typing import Optional

from django.db.models import QuerySet

from main.models import Organization
from main.views.organization_switched_mixin import OrganizationSwitchedMixin


class OrganizationObjectMixin(OrganizationSwitchedMixin):
    def get_object(
        self, _queryset: Optional[QuerySet[Organization]] = None
    ) -> Organization:
        """Override object with switched organization."""
        return Organization.objects.get(pk=self.organization_id)
