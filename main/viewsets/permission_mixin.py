from typing import Any, Sequence

from rest_framework.permissions import BasePermission
from rest_framework.viewsets import GenericViewSet


class PermissionMixin(GenericViewSet[Any]):
    permission_dict: dict[str, tuple[type[BasePermission]]]

    def get_permissions(self) -> Sequence[BasePermission]:
        """Get permissions based on action."""
        return [
            permission() for permission in self.permission_dict.get(self.action, [])
        ]
