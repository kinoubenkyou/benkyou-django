from rest_framework.permissions import BasePermission
from rest_framework.viewsets import GenericViewSet


class PermissionMixin(GenericViewSet):
    permission_dict: dict[str, tuple[type[BasePermission]]]

    def get_permissions(self):  # type: ignore[no-untyped-def]
        """Get permissions based on action."""
        return [
            permission() for permission in self.permission_dict.get(self.action, [])
        ]
