from typing import Tuple

from django.views.generic.detail import DetailView


class ReadView(DetailView):
    field_names: tuple[str, ...]
    template_name = "read.html"  # type: ignore[assignment]

    def get_context_data(self, **kwargs):  # type: ignore[no-untyped-def]
        """Add tuples of the object's field name and field value to the context."""
        return_ = super().get_context_data(**kwargs)  # type: ignore[no-untyped-call]
        return_.update(
            object_fields=tuple(
                (field_name, getattr(self.object, field_name))
                for field_name in self.field_names
            )
        )
        return return_
