from typing import Any

from django.core.cache import cache
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main.models import User
from main.serializers.user.create import UserCreateSerializer
from main.serializers.user.read import UserReadSerializer
from main.serializers.user.update import UserUpdateSerializer
from main.serializers.user.verify_email import UserVerifyEmailSerializer
from main.tasks.start_verify_user_email import start_verify_user_email
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
        "verify_email": UserVerifyEmailSerializer,
    }
    permission_dict = {
        "retrieve": (IsAuthenticated,),
        "update": (IsAuthenticated,),
        "partial_update": (IsAuthenticated,),
        "destroy": (IsAuthenticated,),
        "start_verify_email": (IsAuthenticated,),
        "verify_email": (IsAuthenticated,),
    }

    def get_object(self) -> User:
        """Get authenticated user."""
        user = self.request.user
        self.check_object_permissions(self.request, user)
        return user  # type: ignore[return-value]

    @action(detail=False, methods=["post"])
    def start_verify_email(self, request: Request) -> Response:
        """Queue task to start verify email."""
        start_verify_user_email.delay(
            request.get_host(), request.scheme, request.user.pk
        )
        return Response()

    @action(detail=False, methods=["post"])
    def verify_email(self, request: Request) -> Response:
        """Set the email as verified, delete the token from the cache."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.request.user.email_is_verified = True  # type: ignore[union-attr]
        self.request.user.save()
        cache.delete(f"verify_user_email.{self.request.user.id}")
        return Response()
