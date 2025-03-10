from rest_framework.serializers import ModelSerializer

from main.models import User


class UserReadSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "last_login",
            "first_name",
            "last_name",
            "email",
            "date_joined",
        )
