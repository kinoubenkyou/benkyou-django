from typing import Any, Sequence

from django.db.models import QuerySet
from rest_framework.filters import OrderingFilter
from rest_framework.request import Request
from rest_framework.views import APIView


class FilterBackend(OrderingFilter):
    ordering_param = "sort_by"

    def filter_queryset(
        self, request: Request, queryset: QuerySet[Any], view: APIView
    ) -> QuerySet[Any]:
        """Filter queryset based on query params."""
        filter_set = view.filter_set_class(data=request.query_params, partial=True)  # type: ignore[attr-defined]
        filter_set.is_valid(raise_exception=True)
        return queryset.filter(**filter_set.validated_data).order_by(
            *self.get_ordering(request, queryset, view)  # type: ignore[misc]
        )

    def get_default_ordering(self, view: APIView) -> Sequence[str] | None:
        """Set default ordering to id."""
        return super().get_default_ordering(view) or ("id",)
