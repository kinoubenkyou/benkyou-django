from typing import Any

from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer
from rest_framework.settings import DEFAULTS

from main.models import User


class UserResetPasswordSerializer(Serializer[None]):
    password = CharField()
    token = CharField()
    username = CharField()

    def validate(self, attrs: Any) -> Any:
        """Validate with token in cache."""
        errors = []
        sentinel = object()
        token = cache.get(f"reset_user_password.{attrs['username']}", sentinel)
        if token is sentinel:
            errors.append("token not found")
        elif token != attrs["token"]:
            errors.append("incorrect token")
        if errors:
            raise ValidationError({DEFAULTS["NON_FIELD_ERRORS_KEY"]: errors})
        return attrs

    @staticmethod
    def validate_username(value: str) -> str:
        """Validate username found."""
        if not User.objects.filter(username=value).exists():
            raise ValidationError("username not found")
        return value
