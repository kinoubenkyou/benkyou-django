from django.contrib.auth.password_validation import (
    password_validators_help_text_html,
    validate_password,
)
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from main.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "last_login",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "password",
        )

    password = CharField(
        help_text=password_validators_help_text_html(),
        write_only=True,
        validators=(validate_password,),
    )

    def create(self, validated_data):  # type: ignore[no-untyped-def]
        """Create user."""
        return_ = super().create(validated_data)  # type: ignore[no-untyped-call]
        return_.set_password(validated_data["password"])
        return_.save()
        return return_
