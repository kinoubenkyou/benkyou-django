from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet


class SerializerMixin(GenericViewSet):
    serializer_dict: dict[str, type[Serializer]]

    def get_serializer_class(self):  # type: ignore[no-untyped-def]
        """Get serializer based on action."""
        return self.serializer_dict[self.action]
