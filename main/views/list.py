from typing import TYPE_CHECKING, Any

from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView as DjangoListView

from main.forms.list import ListForm

if TYPE_CHECKING:
    ListView_ = DjangoListView[Any]  # pragma: no cover
else:
    ListView_ = DjangoListView


class ListView(ListView_):
    form_class = ListForm
    object_fields: tuple[str, ...] = tuple()
    paginate_by = 50
    template_name = "list.html"

    def get(self, request: HttpRequest, *_args: Any, **_kwargs: Any) -> HttpResponse:
        """Set default page size, paginating, ordering, filtering, render response."""
        data = request.GET.copy()
        data.setdefault("page_size", str(self.paginate_by))
        data.setdefault("sort_by", "id")
        form = self.form_class(data=data)
        if form.is_valid():
            self.paginate_by = form.cleaned_data["page_size"]
            self.ordering = form.cleaned_data["sort_by"]
            self.object_list = self.get_queryset().filter(
                **{
                    filter_field: form.cleaned_data[filter_field]
                    for filter_field in form.cleaned_data
                    if filter_field in form.Meta.filter_fields
                }
            )
        else:
            self.object_list = self.get_queryset().none()
        return self.render_to_response(
            self.get_context_data(form=form, object_fields=self.object_fields)
        )
