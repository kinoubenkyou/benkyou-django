from typing import Any

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT


class UserTokenApiView(ObtainAuthToken):
    permission_mapping = {"DELETE": (IsAuthenticated,)}

    def delete(
        self, request: Request, *args: tuple[Any, ...], **kwargs: dict[str, Any]
    ) -> Response:
        """Handle DELETE request."""
        self.get_object().delete()  # type: ignore[no-untyped-call]
        return Response(status=HTTP_204_NO_CONTENT)

    def get_object(self):  # type: ignore[no-untyped-def]
        """Get authenticated token."""
        token = self.request.auth
        self.check_object_permissions(self.request, token)  # type: ignore[no-untyped-call]
        return token

    def get_permissions(self):  # type: ignore[no-untyped-def]
        """Get permissions based on request method."""
        return [
            permission()
            for permission in self.permission_mapping.get(self.request.method, [])
        ]
