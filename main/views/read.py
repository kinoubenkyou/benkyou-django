from typing import TYPE_CHECKING, Any

from django.views.generic.detail import DetailView

from main.models import User

if TYPE_CHECKING:
    DetailView_ = DetailView[User]  # pragma: no cover
else:
    DetailView_ = DetailView


class ReadView(DetailView_):
    field_names: tuple[str, ...]
    template_name = "read.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Add tuples of the object's field name and field value to the context."""
        DetailView.get_context_data(self, **kwargs)
        return_ = super().get_context_data(**kwargs)
        return_.update(
            object_fields=tuple(
                (field_name, getattr(self.object, field_name))
                for field_name in self.field_names
            )
        )
        return return_
