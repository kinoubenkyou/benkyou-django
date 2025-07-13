from rest_framework.serializers import ModelSerializer

from main.models import Organization


class OrganizationsSerializer(ModelSerializer[Organization]):
    class Meta:
        model = Organization
        fields = ("code", "name")
