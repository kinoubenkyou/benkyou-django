from typing import Tuple

from django.views.generic.detail import DetailView


class ReadView(DetailView):
    excluded_fields: Tuple[str, ...]
    template_name = "read.html"  # type: ignore[assignment]

    def get_context_data(self, **kwargs):  # type: ignore[no-untyped-def]
        return_ = super().get_context_data(**kwargs)  # type: ignore[no-untyped-call]
        return_.update(
            object_fields=(
                (field.name, getattr(self.object, field.name))
                for field in self.object._meta.fields
                if field.name not in self.excluded_fields
            )
        )
        return return_
