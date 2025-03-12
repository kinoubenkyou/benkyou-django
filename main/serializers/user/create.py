from typing import Any

from django.contrib.auth.password_validation import (
    password_validators_help_text_html,
    validate_password,
)
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from main.models import User


class UserCreateSerializer(ModelSerializer[User]):
    class Meta:
        model = User
        fields = (
            "password",
            "username",
            "first_name",
            "last_name",
            "email",
        )

    password = CharField(
        help_text=password_validators_help_text_html(),
        write_only=True,
        validators=(validate_password,),
    )

    def create(self, validated_data: Any) -> User:
        """Create user."""
        return_ = super().create(validated_data)
        return_.set_password(validated_data["password"])
        return_.save()
        return return_
