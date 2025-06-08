from django.views.decorators.debug import sensitive_variables
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class UserUpdatePasswordSerializer(Serializer[None]):
    old_password = CharField()
    new_password = CharField()

    @sensitive_variables("value")
    def validate_old_password(self, value: str) -> str:
        """Validate with user password."""
        if not self.context.get("request").user.check_password(value):
            raise ValidationError("incorrect old password")
        return value
