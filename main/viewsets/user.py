from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from main.models import User
from main.serializers import UserSerializer


class UserViewSet(CreateModelMixin, GenericViewSet):  # type: ignore[misc]
    queryset = User.objects.all()
    serializer_class = UserSerializer  # type: ignore[assignment]
