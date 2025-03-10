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


class UserViewSet(  # type: ignore[misc]
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    PermissionMixin,
    SerializerMixin,
    GenericViewSet,
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

    def get_object(self):  # type: ignore[no-untyped-def]
        """Get authenticated user."""
        user = self.request.user
        self.check_object_permissions(self.request, user)  # type: ignore[no-untyped-call]
        return user
