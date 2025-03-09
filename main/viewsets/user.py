from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from main.models import User
from main.serializers import UserSerializer


class UserViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):  # type: ignore[misc]
    queryset = User.objects.all()
    serializer_class = UserSerializer  # type: ignore[assignment]
    permission_mapping = {"retrieve": (IsAuthenticated,)}

    def get_object(self):  # type: ignore[no-untyped-def]
        """Get authenticated user."""
        user = self.request.user
        self.check_object_permissions(self.request, user)  # type: ignore[no-untyped-call]
        return user

    def get_permissions(self):  # type: ignore[no-untyped-def]
        """Get permissions based on action."""
        return [
            permission() for permission in self.permission_mapping.get(self.action, [])
        ]
