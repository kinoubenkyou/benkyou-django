from rest_framework.serializers import ModelSerializer

from main.models import User


class UserReadSerializer(ModelSerializer[User]):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "email_is_verified",
        )
