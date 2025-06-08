from typing import Any

from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from main.models import User
from main.tasks.start_verify_user_email import start_verify_user_email


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

    password = CharField()

    def create(self, validated_data: Any) -> User:
        """Set password, queue task to start verify email."""
        validated_data["email_is_verified"] = False
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        start_verify_user_email.delay(
            self.context["request"].get_host(), self.context["request"].scheme, user.pk
        )
        return user
