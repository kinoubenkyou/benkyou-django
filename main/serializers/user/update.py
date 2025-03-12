from rest_framework.serializers import ModelSerializer

from main.models import User


class UserUpdateSerializer(ModelSerializer[User]):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )
