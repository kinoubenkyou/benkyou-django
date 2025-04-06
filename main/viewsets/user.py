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
from main.serializers.user.create import UserCreateSerializer
from main.serializers.user.read import UserReadSerializer
from main.serializers.user.update import UserUpdateSerializer
from main.viewsets.permission_mixin import PermissionMixin
from main.viewsets.serializer_mixin import SerializerMixin


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
        "partial_update": UserUpdateSerializer,
    }
    permission_dict = {
        "retrieve": (IsAuthenticated,),
        "update": (IsAuthenticated,),
        "partial_update": (IsAuthenticated,),
        "destroy": (IsAuthenticated,),
    }

    def get_object(self) -> User:
        """Get authenticated user."""
        user = self.request.user
        assert user.is_authenticated
        self.check_object_permissions(self.request, user)
        return user
