from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from main.filter_sets.organizations import OrganizationsFilterSet
from main.models import Organization
from main.serializers.organizations import OrganizationsSerializer
from main.viewsets.permission_mixin import PermissionMixin
from main.viewsets.serializer_mixin import SerializerMixin


class OrganizationsViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    PermissionMixin,
    SerializerMixin,
    GenericViewSet[Organization],
):
    filter_set_class = OrganizationsFilterSet
    ordering_fields = ("code", "name")
    permission_dict = {
        "list": (IsAuthenticated,),
        "retrieve": (IsAuthenticated,),
    }
    queryset = Organization.objects.all()
    serializer_dict = {
        "list": OrganizationsSerializer,
        "retrieve": OrganizationsSerializer,
    }
