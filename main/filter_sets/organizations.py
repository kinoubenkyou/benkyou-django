from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class OrganizationsFilterSet(Serializer[None]):
    code__icontains = CharField()
    name__icontains = CharField()
