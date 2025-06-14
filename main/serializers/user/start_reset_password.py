from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer

from main.models import User


class UserStartResetPasswordSerializer(Serializer[None]):
    username = CharField(write_only=True)

    @staticmethod
    def validate_username(value: str) -> str:
        """Validate the old password."""
        if not User.objects.filter(username=value).exists():
            raise ValidationError("username not found")
        return value
