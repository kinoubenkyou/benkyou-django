from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from main.models import User
from main.serializers import UserSerializer
from main.viewsets import PermissionMixin


class UserViewSet(  # type: ignore[misc]
    CreateModelMixin, RetrieveModelMixin, PermissionMixin, GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # type: ignore[assignment]
    permission_dict = {"retrieve": (IsAuthenticated,)}

    def get_object(self):  # type: ignore[no-untyped-def]
        """Get authenticated user."""
        user = self.request.user
        self.check_object_permissions(self.request, user)  # type: ignore[no-untyped-call]
        return user
