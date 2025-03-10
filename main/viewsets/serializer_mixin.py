from typing import Any

from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet


class SerializerMixin(GenericViewSet[Any]):
    serializer_dict: dict[str, type[Serializer[Any]]]

    def get_serializer_class(self) -> type[Serializer[Any]]:
        """Get serializer based on action."""
        return self.serializer_dict[self.action]
