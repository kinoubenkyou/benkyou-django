from typing import Any, Sequence

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT


class UserTokenApiView(ObtainAuthToken):
    permission_mapping = {"DELETE": (IsAuthenticated,)}

    def delete(
        self, request: Request, *args: tuple[Any, ...], **kwargs: dict[str, Any]
    ) -> Response:
        """Handle DELETE request."""
        self.get_object().delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def get_object(self) -> Token:
        """Get authenticated token."""
        token = self.request.auth
        self.check_object_permissions(self.request, token)
        return token

    def get_permissions(self) -> Sequence[BasePermission]:
        """Get permissions based on request method."""
        return [
            permission()
            for permission in self.permission_mapping.get(self.request.method, [])  # type: ignore[arg-type]
        ]
