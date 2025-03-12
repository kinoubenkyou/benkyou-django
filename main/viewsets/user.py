from typing import Any

from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from main.models import User
from main.serializers.user import (
    UserCreateSerializer,
    UserReadSerializer,
    UserUpdateSerializer,
)
from main.viewsets import PermissionMixin, SerializerMixin


class UserViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    PermissionMixin,
    SerializerMixin,
    GenericViewSet[Any],
):
    queryset = User.objects.all()
    serializer_dict = {
        "create": UserCreateSerializer,
        "retrieve": UserReadSerializer,
        "update": UserUpdateSerializer,
    }
    permission_dict = {
        "retrieve": (IsAuthenticated,),
        "update": (IsAuthenticated,),
        "destroy": (IsAuthenticated,),
    }

    def get_object(self) -> User:
        """Get authenticated user."""
        user = self.request.user
        assert user.is_authenticated
        self.check_object_permissions(self.request, user)
        return user
