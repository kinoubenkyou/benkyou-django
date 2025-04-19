from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class UserVerifyEmailSerializer(Serializer[None]):
    token = CharField(write_only=True)

    def validate_token(self, value: str) -> str:
        """Validate with token in cache."""
        sentinel = object()
        token = cache.get(
            f"verify_user_email.{self.context['request'].user.id}", sentinel
        )
        if token is sentinel:
            raise ValidationError("token not found")
        elif token != value:
            raise ValidationError("incorrect token")
        return value
