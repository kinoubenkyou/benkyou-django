from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import (
    validate_password,
)
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class UserUpdatePasswordSerializer(Serializer[None]):
    old_password = CharField()
    new_password = CharField(write_only=True, validators=(validate_password,))

    def validate_old_password(self, value: str) -> str:
        """Validate the old password."""
        request = self.context.get("request")
        user = authenticate(
            request=request,
            username=request.user.username,  # type: ignore[union-attr]
            password=value,
        )
        if not user:
            raise ValidationError("incorrect old password")
        return value
