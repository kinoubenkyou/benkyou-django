from typing import TYPE_CHECKING, Any

from django.views.generic.detail import DetailView

if TYPE_CHECKING:
    DetailView_ = DetailView[Any]  # pragma: no cover
else:
    DetailView_ = DetailView


class ReadView(DetailView_):
    object_fields: tuple[str, ...]
    template_name = "read.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Add object's field names to context."""
        context_data = super().get_context_data(**kwargs)
        context_data.update(object_fields=self.object_fields)
        return context_data
